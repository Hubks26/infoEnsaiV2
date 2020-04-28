from gestion.elements_fichiers.elm_fichier import Elm_Fichier

class Compte(Elm_Fichier):
	def __init__(self, pseudo, mot_de_passe, statut):
		super().__init__("comptes")
		self.pseudo = pseudo
		self.mot_de_passe = mot_de_passe
		self.statut = statut

	def __eq__(self, autre_compte):
		return self.pseudo == autre_compte.pseudo and self.mot_de_passe == autre_compte.mot_de_passe
