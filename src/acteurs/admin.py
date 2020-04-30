from affichage.menu_ouvert import Menu_Ouvert
from acteurs.geographe import Geographe
from acteurs.data_scientist import Data_Scientist
from gestion.elements_fichiers.compte import Compte
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Admin(Geographe, Data_Scientist):
	def __init__(self):
		super().__init__()
		self.statut = 'a'
		
	def gestion_compte(self, contenu):
		if self.verification_connexion():
			choix_gestion = {}
			choix_gestion['pseudo'] = contenu['pseudo']
			choix_gestion['individu'] = contenu['individu']
			choix_gestion['question'] = 'Que voulez vous faire ?'
			choix_gestion['options'] = ['Créer un compte', 'Supprimer un compte', 'Voir la liste des comtpes']
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
				mot_de_passe = input("Entrez le mot de passe : ")
				if len(mot_de_passe) >= 4:
					break
				print("\nVotre mot de passe doit contenir au moins 4 caractères.\n")
			mot_de_passe_confirmation = input("Confirmez le mot de passe : ")
			if mot_de_passe == mot_de_passe_confirmation:
				break
			print("\nLa confirmation ne correspond pas au mot de passe initial.\n")
			
		gestionnaire.save_elm(Compte(pseudo, mot_de_passe, type_de_compte))
		input("\nLe compte a bien été enregistré.\nAppuyez sur entrer pour continuer.")
		return Menu_Ouvert(contenu)
		
	def _supprimer_compte(self, contenu):
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		
		pseudo_compte_a_supprimer = input('\nEntrez le pseudo du compte à supprimer\n> ')
		if pseudo_compte_a_supprimer != contenu['pseudo']:
			gestionnaire.suppr_elm(Compte(pseudo_compte_a_supprimer))
		else:
			input('\nVous ne pouvez pas supprimer votre propre compte.\nAppuyez sur entrer pour continuer.')
		return Menu_Ouvert(contenu)
	
	def _afficher_liste_des_comptes(self, contenu):
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		
		print('\n--------------------------------')
		for compte in liste_des_comptes:
			print(compte)
			print('\n--------------------------------')
		input('\nAppuyez sur entrer pour continuer.')
			
		return Menu_Ouvert(contenu)
