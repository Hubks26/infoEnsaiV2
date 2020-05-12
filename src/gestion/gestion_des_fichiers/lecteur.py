import pickle

class Lecteur:
	"""Cette classe s'occupe de lire et d'écrire dans un fichier correspondant"""
	
	def __init__(self):
		pass
	
	def read(self, chemin_du_fichier):
		"""Permet de lire le contenu du fichier"""
		try:
			with open(chemin_du_fichier, 'rb') as fichier:
				unpickler = pickle.Unpickler(fichier)
				contenu = unpickler.load()
		except FileNotFoundError:
			contenu = []
			self.write(chemin_du_fichier, contenu)
		return contenu
	
	def write(self, chemin_du_fichier, contenu):
		"""permet d'écrire du contenu dans le fichier"""
		
		with open(chemin_du_fichier, 'wb') as fichier:
			pickler = pickle.Pickler(fichier)
			contenu = pickler.dump(contenu)
