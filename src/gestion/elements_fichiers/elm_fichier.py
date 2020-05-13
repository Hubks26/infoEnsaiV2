
class Elm_Fichier:
	"""Cette classe permet de trouver les différents fichiers qui seront utilisés 
	par l'application, comme la base de données"""
	
	def __init__(self, nom_fichier):
		self.chemin = "../media/files/"
		self.nom_fichier = nom_fichier

	def get_chemin_fichier(self):
		"""Cette méthode renvoie le chemin d'un fichier"""
		
		return self.chemin + self.nom_fichier
