from acteurs.individu import Individu
from gestion.elements_fichiers.section import Section
from gestion.elements_fichiers.proposition_correction import Proposition_Correction
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.section import Section
from gestion.elements_fichiers.pays import Pays
from affichage.menu_ouvert import Menu_Ouvert

class Consultant(Individu):
	# Cette classe hérite de la classe Individu. Il s'agit d'un acteur.
	# Le statut du consultant est "consultant"
	
	def __init__(self):
		super().__init__()
		self.statut = 'c'
		
	def afficher_pays(self, contenu):
		if self.contenu_initial == {}:
			self.contenu_initial = contenu
			
		donnees = Data_Base().donnees
		nb_pays = len(donnees)
		
		choix_pays = {}
		choix_pays['question'] = 'Choisissez un pays.'
		choix_pays['individu'] = contenu['individu']
		
		liste_des_pays = []
		for num_pays in range(nb_pays):
			nom_pays = Pays(num_pays, donnees).get_name()
			if nom_pays:
				liste_des_pays.append((nom_pays, num_pays))
		liste_des_pays.sort()
		
		liste_des_noms = [pays[0] for pays in liste_des_pays]
		liste_des_nums = [pays[1] for pays in liste_des_pays]
		
		choix_pays['options'] = liste_des_noms
		choix_pays['options basiques'] = []
		choix_pays['actions'] = [lambda var, num=num : self.afficher_section(Section(num, donnees), contenu) for num in liste_des_nums]

		if self.statut == 'g' or self.statut == 'a':
			choix_pays['options basiques'].append(['AJOUTER UN PAYS', 'A'])
			choix_pays['actions'].append(lambda var : self.ajout_pays(contenu))
		if self.statut == 'a':
			choix_pays['options basiques'].append(['SUPPRIMER UN PAYS', 'S'])
			choix_pays['actions'].append(lambda var : self.supprimer_pays(contenu))
		choix_pays['options basiques'].append(["RETOUR AU MENU DE L'ACTEUR", 'R'])
		choix_pays['actions'].append(lambda var : Menu_Ouvert(self.contenu_initial))
		choix_pays['options basiques'].append(['QUITTER', 'Q'])
		choix_pays['actions'].append(self.quitter)
		
		return Menu_Ouvert(choix_pays)
	
	def afficher_section(self, section, contenu):
		donnees = Data_Base().donnees
		num_pays = section.num_pays
		chemin = section.chemin
		
		choix_section = {}
		
		chemin_a_afficher = Pays(section.num_pays, donnees).get_name()
		for partie in chemin:
			chemin_a_afficher += ' -> {}'.format(partie)
		
		if section.is_section_de_texte():
			print('\n{} :\n'.format(chemin_a_afficher))
			print(section.contenu['text'])

			self.correction(choix_section, section)
			
			return self.afficher_section(Section(num_pays, donnees, chemin[:-1]), contenu)
		
		sous_sections = section.get_noms_sous_sections()
		
		if len(sous_sections) == 0:
			choix_section['question'] = '{}\n\nCette section est vide.'.format(chemin_a_afficher)
		else :
			choix_section['question'] = '{}\n\nChoisissez une option.'.format(chemin_a_afficher)
			
		choix_section['individu'] = contenu['individu']
		choix_section['options'] = sous_sections
		choix_section['options basiques'] = []
		choix_section['actions'] = []
		
		for partie in sous_sections:
			nouveau_chemin = chemin + [partie]
			choix_section['actions'].append((lambda contenu, nouveau_chemin=nouveau_chemin : self.afficher_section(Section(num_pays, donnees, nouveau_chemin), contenu)))
			
		if self.statut == 'g' or self.statut == 'a':
			if len(sous_sections) == 0:
				choix_section['options basiques'].append(['AJOUTER UN TEXTE', 'AT'])
				choix_section['actions'].append(lambda var : self.ajout_texte(contenu, section))
			choix_section['options basiques'].append(['AJOUTER UNE SECTION', 'AS'])
			choix_section['actions'].append(lambda var : self.ajout_section(contenu, section))
		if self.statut == 'a' and len(sous_sections) != 0:
			choix_section['options basiques'].append(['SUPPRIMER UNE SECTION', 'S'])
			choix_section['actions'].append(lambda var : self.supprimer_section(contenu, section))
				
		choix_section['options basiques'].append(['RETOUR', 'R'])
		if len(chemin) == 0:
			choix_section['actions'].append(lambda var : self.afficher_pays(contenu))
		else:
			choix_section['actions'].append(lambda var : self.afficher_section(Section(num_pays, donnees, chemin[:-1]), contenu))
		choix_section['options basiques'].append(["RETOUR AU MENU DE L'ACTEUR", 'RMA'])
		choix_section['actions'].append(lambda contenu : Menu_Ouvert(self.contenu_initial))
		choix_section['options basiques'].append(['QUITTER', 'Q'])
		choix_section['actions'].append(self.quitter)
		
		return Menu_Ouvert(choix_section)

	def correction(self, contenu, section):
		# Cette méthode permet de proposer une correction.
		# Elle prend en argument un contenu et ne renvoie rien.
		# L'utilisateur n'a qu'à entrer la proposition de 
		# correction afin de l'enregistrer.
		
		chemin = section.chemin
		num_pays = section.num_pays
		
		if chemin[-1] == 'conventional short form' or chemin[-1] == 'conventional long form':
			input('\nVous ne pouvez pas proposer de correction pour le nom du pays.\nAppuyez sur entrer pour continuer.')
		else:
			rep = input('\nVoulez vous proposer une correction (O/N) ?\n> ')
			if rep in ['o', 'O']:
				while True:
					txt_correction = input('\nEntrez la proposition de correction :\n> ')
					if len(txt_correction) > 1:
						break
					print('\nVotre texte doit contenir au moins 1 caractère\n')
					
				prop_correction = Proposition_Correction(txt_correction, num_pays, chemin)
				gestionnaire = Gestionnaire()
				gestionnaire.save_elm(prop_correction)

				continuer = input('\nVotre proposition de correction a bien été enregistrée.\nAppuyez sur entrer pour continuer.')
