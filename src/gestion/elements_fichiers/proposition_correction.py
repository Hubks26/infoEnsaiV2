from gestion.elements_fichiers.elm_fichier import Elm_Fichier

class Proposition_Correction(Elm_Fichier):
	def __init__(self, txt_prop, num_pays, chemin_prop):
		super().__init__("props_corrections")
		self.txt_prop = txt_prop
		self.num_pays = num_pays
		self.chemin_prop = chemin_prop

	def __str__(self):
		return self.txt_prop
