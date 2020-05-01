from affichage.menu_ouvert import Menu_Ouvert
from affichage.menu_ferme import Menu_Ferme
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.section import Section
from gestion.elements_fichiers.pays import Pays

class Individu:
	# Classe mère des classes Consultant.
	
	def __init__(self):
		self.statut = None
		self.contenu_initial = {}
		
	def quitter(self, contenu):
		# Cette méthode est commune à tous les individus. Elle prend en argument
		# un contenu de menu (dict) et renvoie un menu ouvert ou fermé selon la
		# confirmation de l'utilisateur.
		
		confirmation = input('\nVoulez-vous vraiment quitter (O/N) ?\n> ')
		if confirmation in ['o', 'O']:
			return Menu_Ferme(contenu)
		else:
			return Menu_Ouvert(contenu)
	
	def afficher_pays(self, contenu):
		if self.contenu_initial == {}:
			self.contenu_initial = contenu
			
		donnees = Data_Base().donnees
		nb_pays = len(donnees)
		
		choix_pays = {}
		choix_pays['question'] = 'Choisissez un pays.'
		choix_pays['individu'] = contenu['individu']
		choix_pays['chemin de la recherche'] = []
		
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
			choix_pays['actions'].append(lambda var : self.supprimer_pays(contenu, var))
		choix_pays['options basiques'].append(["RETOUR AU MENU DE L'ACTEUR", 'R'])
		choix_pays['actions'].append(lambda var : Menu_Ouvert(self.contenu_initial))
		choix_pays['options basiques'].append(['QUITTER', 'Q'])
		choix_pays['actions'].append(self.quitter)
		
		return Menu_Ouvert(choix_pays)
	
	def afficher_section(self, section, contenu): # En faire une méthode privée ?
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
			choix_section['actions'].append(lambda var : self.supprimer_section(var, contenu))
				
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
		raise NotImplemented()
		
	def ajout_section(self, contenu, section):
		raise NotImplemented()
	
	def ajout_texte(self, contenu, section):
		raise NotImplemented()

	def ajout_pays(self, contenu):
		raise NotImplemented()

	def supprimer_section(self, contenu, contenu_precedent):
		raise NotImplemented()

	def supprimer_pays(self, contenu, contenu_precedent):
		raise NotImplemented()
