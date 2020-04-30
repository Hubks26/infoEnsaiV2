from gestion.elements_fichiers.elm_fichier import Elm_Fichier

class Compte(Elm_Fichier):
	def __init__(self, pseudo=None, mot_de_passe=None, statut=None):
		super().__init__("comptes")
		self._pseudo = pseudo
		self._mot_de_passe = mot_de_passe
		self._statut = statut

	def __eq__(self, autre_compte):
		return self._pseudo == autre_compte.get_pseudo()
	
	def __str__(self):
		return '\n   Pseudo : {}\n   Statut : {}\n   Mot de passe : {}'.format(self._pseudo, self._statut, self._mot_de_passe)
	
	def get_pseudo(self):
		return self._pseudo
	
	def get_statut(self):
		return self._statut
	
	def get_mot_de_passe(self):
		return self._mot_de_passe
