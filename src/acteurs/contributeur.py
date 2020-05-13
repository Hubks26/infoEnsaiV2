import getpass as gp
from affichage.menu_ouvert import Menu_Ouvert
from acteurs.consultant import Consultant
from gestion.elements_fichiers.compte import Compte
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Contributeur(Consultant):
	""" Cette classe ne représente pas un acteur.
	Elle permet aux acteurs qui en hériteront, de se connecter afin d'accéder à 
	leurs différentes tâches"""
	
	def __init__(self):
		"""Le statut de cette classe est None"""
		
		super().__init__()
		self.est_connecte = False
		self.statut = None
		
	def verification_connexion(self):
		"""Méthode qui permet de savoir si l'acteur est connecté ou non.
		S'il ne l'est pas, il renvoie un message d'erreur"""
		
		if not self.est_connecte:
			input("\nVEUILLEZ D'ABORD VOUS CONNECTER.\nAppuyez sur entrer pour continuer.")
			return False
		return True
	
	def se_connecter(self, contenu):
		"""Cette méthode permet à l'acteur de se connecter.
		L'individu entre son pseudo et son mot de passe. Il sera comparé au 
		gestionnaire des comptes."""
		
		gestionnaire = Gestionnaire()
		liste_des_comptes = gestionnaire.read(Compte().get_chemin_fichier())
		
		pseudo = input("\nEntrez votre pseudo : ")
		mot_de_passe = gp.getpass("Entrez votre mot de passe : ")
		
		for compte in liste_des_comptes:
			if self.statut == compte.get_statut() and pseudo == compte.get_pseudo() and mot_de_passe == compte.get_mot_de_passe():
				self.est_connecte = True
				del contenu['options'][0]
				del contenu['actions'][0]
				contenu['pseudo'] = pseudo
				print("\nVous êtes connecté !")
				input("Appuyez sur entrer pour continuer.")
				return Menu_Ouvert(contenu)
			
		print("\nVotre connexion a échouée.")
		input("Appuyez sur entrer pour continuer.")
		return Menu_Ouvert(contenu)
