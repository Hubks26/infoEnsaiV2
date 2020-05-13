from affichage.menu_ouvert import Menu_Ouvert
from acteurs.contributeur import Contributeur
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.section import Section
from gestion.elements_fichiers.pays import Pays
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Geographe(Contributeur):
	"""Cette classe correspond à la classe du géographe."""
	
	def __init__(self):
		"""son statut est la lettre 'g'"""
		
		super().__init__()
		self.statut = 'g'
		
	def correction(self, contenu, section_de_texte):
		""" La méthode correction prend en compte un contenu de menu et un texte.
		Elle permet la modification d'une information par un nouveau texte."""
		
		gestionnaire = Gestionnaire()
		chemin = section_de_texte.chemin
		
		if chemin[-1] == 'conventional short form' or chemin[-1] == 'conventional long form':
			input('\nVous ne pouvez pas modifier le nom du pays.\nAppuyez sur entrer pour continuer.')
		else:
			rep = input('\nVoulez vous modifier le texte (O/N) ?\n> ')
			if rep in ['o', 'O']:
				if self.verification_connexion():
					while True:
						txt_correction = input('\nEntrez le nouveau texte :\n> ')
						if len(txt_correction) > 1:
							break
						print('\nVotre texte doit contenir au moins 1 caractère\n')
						
					section_de_texte.contenu['text'] = txt_correction
					
					confirmation = input('\nConfirmation de la modification #Cela écrasera le texte initial# (O/N) ?\n> ')
					if confirmation in ["o","O"]:
						gestionnaire.update(section_de_texte.donnees)
						input('\nVotre modification a bien été enregistrée.\nAppuyez sur entrer pour continuer.')
					else :
						input("\nVotre tentative de modification n'a pas abouti.\nAppuyez sur entrer pour continuer.")
						
	def ajout_texte(self, contenu, section):
		"""La méthode ajout_texte permet d'ajouter un texte à une section donnée"""
		
		gestionnaire = Gestionnaire()
		section_mere = Section(section.num_pays, section.donnees, section.chemin[:-1])
		
		if self.verification_connexion():
			while True:
				texte = input('\nEntrez le texte à ajouter :\n> ')
				if len(texte) <= 1:
					input('\nLe nom de la section doit contenir au moins 1 caractère.\nAppuyez sur entrer pour continuer.')
					continue
				break
			
			confirmation = input("\nConfirmation de l'ajout du texte (O/N) ?\n> ")
			if confirmation in ['o', 'O']:
				section.contenu['text'] = texte
				gestionnaire.update(section.donnees)
				input('\nLe texte a bien été ajouté.\nAppuyez sur entrer pour continuer.')
				return self.afficher_section(section_mere, contenu)
			else :
				input("\nVotre tentative d'ajout de texte n'a pas abouti.\nAppuyez sur entrer pour continuer.")
				
		return self.afficher_section(section, contenu)
						
	def ajout_section(self, contenu, section):
		"""Cette méthode permet de créer une nouvelle section dans un pays"""
		
		gestionnaire = Gestionnaire()
		noms_indisponibles = section.get_noms_sous_sections()
		
		if self.verification_connexion():
			while True:
				nom_section = input('\nEntrez le nom de la nouvelle section :\n> ')
				if len(nom_section) <= 1 or len(nom_section) > 50:
					input('\nLe nom de la section doit contenir entre 1 et 50 caractères.\nAppuyez sur entrer pour continuer.')
					continue
				if nom_section in noms_indisponibles:
					input("\nCe nom est déjà celui d'une section existante, veuillez en choisir un autre.\nAppuyez sur entrer pour continuer.")
					continue
				if (nom_section == 'Government') or (nom_section == 'Country name') or (nom_section == 'conventional short form') or (nom_section == 'conventional long form') or (nom_section == 'text'):
					input('\nLa section ne peut pas porter de nom tel que Government, Country name, conventional short form, conventional long form ou text.\nAppuyez sur entrer pour continuer.')
					continue
				break
			
			confirmation = input('\nConfirmation de la création de la section (O/N) ?\n> ')
			if confirmation in ['o', 'O']:
				section.contenu[nom_section] = {}
				gestionnaire.update(section.donnees)
				input('\nLa nouvelle section a été ajoutée.\nAppuyez sur entrer pour continuer.')
			else :
				input("\nVotre tentative d'ajout de section n'a pas abouti.\nAppuyez sur entrer pour continuer.")
				
		return self.afficher_section(section, contenu)

	def ajout_pays(self, contenu):
		"""Cette méthode permet d'ajouter un pays comme la précédente méthode ajout_section"""
		
		gestionnaire = Gestionnaire()
		donnees = Data_Base().donnees
		noms_indisponibles = [Pays(num_pays, donnees).get_name() for num_pays in range(len(donnees)) if Pays(num_pays, donnees).get_name()]
		
		if self.verification_connexion():
			nom_pays = input('\nEntrez le nom du pays à ajouter :\n> ')
			
			if nom_pays == 'none':
				input("\nVous ne pouvez pas nommer un pays 'none'.\nAppyez sur entrer pour continuer.")
				return self.afficher_pays(contenu)
			if nom_pays in noms_indisponibles:
				input('\nCe pays est déjà dans la liste.\nAppyez sur entrer pour continuer.')
				return self.afficher_pays(contenu)
			
			confirmation = input("\nConfirmation de l'ajout du pays (O/N) ?\n> ")
			if confirmation not in ["o","O"]:
				input("\nEchec de l'ajout du pays.\nAppyez sur entrer pour continuer.")
				return self.afficher_pays(contenu)
				
			donnees.append({})
			nouveau_pays = Pays(len(donnees)-1, donnees)
			nouveau_pays.set_name(nom_pays)
			nouveau_pays.set_infos_de_base()
			
			gestionnaire.update(nouveau_pays.donnees)
			input("\nLe pays a bien été ajouté.\nAppuyez sur entrer pour continuer.")

		return self.afficher_pays(contenu)
	
	def gestion_corrections(self, contenu):
		"""La gestion des corrections se fait par cette méthode. Elle affiche les
		différentes propositions que les autres acteurs ont suggérés. Le géographe n'a plus qu'à 
		choisir quelle correction il veut observer"""
		
		gestionnaire = Gestionnaire()
		liste_des_corrections = gestionnaire.read('../media/files/props_corrections')
		
		if self.verification_connexion():
			choix_prop = {}
			choix_prop['pseudo'] = contenu['pseudo']
			choix_prop['individu'] = contenu['individu']
			
			if len(liste_des_corrections) == 0:
				choix_prop['question'] = "Il n'y a pas de propositions à examiner."
			else : 
				choix_prop["question"] = "Choisissez une proposition de correction.\nLe chemin indiqué est celui de l'emplacement du texte susceptible d'être modifié."
				
			choix_prop['options basiques'] = [['RETOUR', 'R'], ['QUITTER', 'Q']]
			choix_prop['options'] = liste_des_corrections
			
			choix_prop['actions'] = [lambda var, prop_cor = prop_cor : self._decider_correction(contenu, prop_cor) for prop_cor in liste_des_corrections]
			choix_prop['actions'].append(lambda var : Menu_Ouvert(contenu))
			choix_prop['actions'].append(self.quitter)

			return Menu_Ouvert(choix_prop)
		else:
			return Menu_Ouvert(contenu)
		
	def _decider_correction(self, contenu, prop_cor):
		"""Cette méthode permet au géographe de choisir entre valider ou refuser
		une proposition de correction."""
		
		donnees = Data_Base().donnees
		gestionnaire = Gestionnaire()
		try :
			section_du_texte = Section(prop_cor.num_pays, donnees, prop_cor.chemin_prop)
		except :
			input('\nIl semble que la donnée initiale a été supprimée. Cette proposition va alors être supprimée.\nAppuyez sur entrer pour continuer')
			gestionnaire.suppr_elm(prop_cor)
			return self.gestion_corrections(contenu)	
		
		print("\nTexte actuel :\n")
		print(section_du_texte.contenu["text"] + "\n")
		print("Proposition de correction :\n")
		print(prop_cor.txt_prop + "\n")
		
		while True:
			validation = input("Voulez-vous valider cette proposition de correction (V : valider / R : refuser / P : aucune action) ?\n> ")
			if validation in ["v","V","r","R","p","P"]:
				break
			else :
				input("\nVotre réponse doit être V, R ou P.\nAppyez sur entrer pour continuer.\n")
				
		if validation in ['v', 'V']:
			self._valider_prop(prop_cor, section_du_texte)
		if validation in ['r', 'R']:
			self._refuser_prop(prop_cor)
			
		return self.gestion_corrections(contenu)
			
	def _refuser_prop(self, prop_cor):
		"""Méthode qui effectue la suppression de la proposition de correction avec une double confirmation"""
		
		gestionnaire = Gestionnaire()
		confirmation = input("\nConfirmation du refus de la proposition (O/N) ? #Cela supprimera la proposition#\n> ")
		if confirmation in ['o', 'O']:
			gestionnaire.suppr_elm(prop_cor)
			input("\nLa proposition a été supprimée !\nAppuyez sur entrer pour continuer.")
		else :
			input("\nVotre tentative de refus n'a pas abouti.\nAppuyez sur entrer pour continuer.")
	
	def _valider_prop(self, prop_cor, section_du_texte):
		"""Méthode qui valide la proposition de correction. Elle va remplacer le texte par la proposition.
		Puis, elle va supprimer la proposition."""
		
		gestionnaire = Gestionnaire()
		confirmation = input("\nConfirmation de la validation du nouveau texte (O/N) ? #Cela supprimera l'ancien texte#\n> ")
		if confirmation in ['o', 'O']:
			section_du_texte.contenu['text'] = prop_cor.txt_prop
			gestionnaire.update(section_du_texte.donnees)
			gestionnaire.suppr_elm(prop_cor)
			input("\nLe texte a bien été modifié !\nAppuyez sur entrer pour continuer.")
		else :
			input("\nVotre tentative de validation n'a pas abouti.\nAppuyez sur entrer pour continuer.")
