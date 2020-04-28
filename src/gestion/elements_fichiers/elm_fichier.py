
class Elm_Fichier:
	def __init__(self, nom_fichier):
		self.chemin = "../media/files/"
		self.nom_fichier = nom_fichier

	def get_chemin_fichier(self):
		return self.chemin + self.nom_fichier
