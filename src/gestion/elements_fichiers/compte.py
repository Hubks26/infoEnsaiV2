from gestion.elements_fichiers.elm_fichier import Elm_Fichier

class Compte(Elm_Fichier):
	"""Cette classe permet de gérer les opérations élémentaires pour les comptes des utilisateurs."""
	
	def __init__(self, pseudo=None, mot_de_passe=None, statut=None):
		"""Permet de créer un nouveau compte utilisateur"""
		
		super().__init__("comptes")
		self._pseudo = pseudo
		self._mot_de_passe = mot_de_passe
		self._statut = statut

	def __eq__(self, autre_compte):
		"""Cette méthode renvoie un booléen pour savoir si un compte existe déjà ou non."""
		
		return self._pseudo == autre_compte.get_pseudo()
	
	def __str__(self):
		"""Affiche les caractéristiques du compte en question."""
		
		return '\n   Pseudo : {}\n   Statut : {}\n   Mot de passe : {}'.format(self._pseudo, self._statut, self._mot_de_passe)
	
	def get_pseudo(self):
		"""Renvoie le pseudo du compte"""
		
		return self._pseudo
	
	def get_statut(self):
		"""renvoie le statut du compte"""
		
		return self._statut
	
	def get_mot_de_passe(self):
		"""renvoie le mot de passe du compte"""
		
		return self._mot_de_passe
