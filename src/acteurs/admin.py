import getpass as gp
from affichage.menu_ouvert import Menu_Ouvert
from acteurs.geographe import Geographe
from acteurs.data_scientist import Data_Scientist
from gestion.elements_fichiers.compte import Compte
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.pays import Pays
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Admin(Geographe, Data_Scientist):
	"""Classe de l'administrateur"""
	def __init__(self):
		"""son staut est la letre 'a'"""
		super().__init__()
		self.statut = 'a'
		
	def gestion_compte(self, contenu):
		"""Cette méthode permet d'acceder aux tâches Suppression/Création d'un compte employeur.
		Elle renvoie les différentes tâches que peut eeffectuer l'administrateur :
		 - Créer un compte
		 - Supprimer un compte
		 - Voir la liste des comptes"""
		
		if self.verification_connexion():
			choix_gestion = {}
			choix_gestion['pseudo'] = contenu['pseudo']
			choix_gestion['individu'] = contenu['individu']
			choix_gestion['question'] = 'Que voulez vous faire ?'
			choix_gestion['options'] = ['Créer un compte', 'Supprimer un compte', 'Voir la liste des comptes']
			choix_gestion['options basiques'] = [['RETOUR', 'R'], ['QUITTER', 'Q']]
			choix_gestion['actions'] = [
				self._creer_compte,
				self._supprimer_compte,
				self._afficher_liste_des_comptes,
				lambda var : Menu_Ouvert(contenu),
				self.quitter]
			return Menu_Ouvert(choix_gestion)
		else:
			return Menu_Ouvert(contenu)
		
	def _creer_compte(self, contenu):
		"""Cette méthode permet à l'administrateur de créer un nouveau compte.
		D'abord, il doit choisir le statut du nouveau acteur. Ensuite son pseudo et enfin son mot de passe.
		Une fois validé, le nouveau compte sera insérer dans le gestionnaire des comptes."""
		
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		liste_des_pseudos = [compte.get_pseudo() for compte in liste_des_comptes]
		
		while True:
			type_de_compte = input('\nVous voulez créer un compte Administrateur, Géographe ou Data Scientist (a/g/d) ? : ')
			if type_de_compte in ['a', 'g', 'd']:
				break
			print('\nLa réponse attendue doit être : a pour Admin, g pour Géographe ou d pour Data Scientist.')
		
		while True:
			pseudo = input('Entrez le pseudo : ')
			if len(pseudo) >= 2:
				if pseudo not in liste_des_pseudos:
					break
				else : print("\nCe pseudo est déjà attribué à quelqu'un, veuillez en choisir un autre.\n")
			else : print('\nVotre pseudo doit contenir au moins 2 caractères.\n')
			
		while True:
			while True:
				mot_de_passe = gp.getpass("Entrez le mot de passe : ")
				if len(mot_de_passe) >= 4:
					break
				print("\nVotre mot de passe doit contenir au moins 4 caractères.\n")
			mot_de_passe_confirmation = gp.getpass("Confirmez le mot de passe : ")
			if mot_de_passe == mot_de_passe_confirmation:
				break
			print("\nLa confirmation ne correspond pas au mot de passe initial.\n")
			
		gestionnaire.save_elm(Compte(pseudo, mot_de_passe, type_de_compte))
		input("\nLe compte a bien été enregistré.\nAppuyez sur entrer pour continuer.")
		return Menu_Ouvert(contenu)
		
	def _supprimer_compte(self, contenu):
		"""A l'inverse de la création d'un compte, cette méthode permet de supprimer un compte.
		L'administrateur n'a besoin que de choisir dans une liste des pseudos des comptes. Cela ne requiert pas le mot de passe
		de l'acteur en question. Une fois effectué, le compte sera supprimé du gestionnaire."""
		
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		liste_des_pseudos = [compte.get_pseudo() for compte in liste_des_comptes]
		
		pseudo_compte_a_supprimer = input('\nEntrez le pseudo du compte à supprimer\n> ')
		
		if pseudo_compte_a_supprimer not in liste_des_pseudos:
			input("\nCe compte n'existe pas.\nAppuyez sur entrer pour continuer.\n")
			return Menu_Ouvert(contenu)
			
		if pseudo_compte_a_supprimer != contenu['pseudo']:
			confirmation = input('\nConfirmation de la suppression du compte (O/N) ?\n> ')
			if confirmation in ['o', 'O']:
				gestionnaire.suppr_elm(Compte(pseudo_compte_a_supprimer))
				input("\nLe compte de {} a bien été supprimé.\nAppuyez sur entrer pour continuer.".format(pseudo_compte_a_supprimer))
			else :
				input("\nLa tentative de suppression de compte n'a pas abouti\nAppuyez sur entrer pour continuer.\n")
		else:
			input('\nVous ne pouvez pas supprimer votre propre compte.\nAppuyez sur entrer pour continuer.')
		return Menu_Ouvert(contenu)
	
	def _afficher_liste_des_comptes(self, contenu):
		"""Cette méthode permet d'afficher la liste des différents comptes qu'il y a dans le gestionnaire"""
		
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		
		print('\n--------------------------------')
		for compte in liste_des_comptes:
			print(compte)
			print('\n--------------------------------')
		input('\nAppuyez sur entrer pour continuer.')
			
		return Menu_Ouvert(contenu)
	
	def supprimer_section(self, contenu, section):
		"""Contrairement au géographe, l'administrateur est le seul à pouvoir supprimer un pays ou une section.
		Ici, cette méthode permet de supprimer une section d'un pays en question.
		Cependant, il ne peut pas supprimer certaines sections comme 'Government' ou 'Country name' car ils contiennent
		la liste des noms des pays."""
		
		gestionnaire = Gestionnaire()
		noms_sous_sections = section.get_noms_sous_sections()
		sections_non_supprimables = ['Government', 'Country name', 'conventional short form', 'conventional long form']
		
		if self.verification_connexion():
			nom_section_a_supprimer = input('\nEntrez le nom de la section à supprimer\n> ')
			if nom_section_a_supprimer not in noms_sous_sections:
				input("\nCette section n'existe pas.\nAppuyez sur entrer pour continuer.")
				return self.afficher_section(section, contenu)
			if nom_section_a_supprimer in sections_non_supprimables:
				input('\nVous ne pouvez pas supprimer cette section car elle est susceptible de contenir le nom du pays.\nAppuyez sur entrer pour continuer.')
				return self.afficher_section(section, contenu)
			
			confirmation = input('\nConfirmation de la suppression de la section (O/N) ? #Cela supprimera aussi toutes ses sous-sections#\n> ')
			if confirmation in ["o","O"]:
				del section.contenu[nom_section_a_supprimer]
				gestionnaire.update(section.donnees)
				input('\nLa section a bien été supprimée.\nAppuyez sur entrer pour continuer.')
			else :
				input("\nVotre tentative de suppression n'a pas abouti.\nAppuyez sur entrer pour continuer.")
			
		return self.afficher_section(section, contenu)
	
	def supprimer_pays(self, contenu):
		"""La méthode supprimer_pays permet de supprimer toutes les données d'un pays, y compris les informations 
		contenu dans les différentes sections."""
		
		gestionnaire = Gestionnaire()
		donnees = Data_Base().donnees
		noms_pays = [Pays(num_pays, donnees).get_name() for num_pays in range(len(donnees))]
		
		if self.verification_connexion():
			nom_pays_a_supprimer = input('\nEntrez le nom du pays à supprimer\n> ')
			if nom_pays_a_supprimer not in noms_pays:
				input("\nCe pays n'existe pas.\nAppuyez sur entrer pour continuer.")
				return self.afficher_pays(contenu)
			else :
				num_pays_a_supprimer = noms_pays.index(nom_pays_a_supprimer)
			
			confirmation = input("\nConfirmation de la suppression du pays (O/N) ? \n> ")
			if confirmation in ["o","O"]:
				del donnees[num_pays_a_supprimer]
				gestionnaire.update(donnees)
				input("\nLe pays a bien été supprimée.\nAppuyez sur entrer pour continuer.")
			else :
				input("\nVotre tentative de suppression n'a pas abouti.\nAppuyez sur entrer pour continuer.")
			
		return self.afficher_pays(contenu)
