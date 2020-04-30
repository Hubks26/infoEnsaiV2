import pickle

class Lecteur:
	def __init__(self):
		pass
	
	def read(self, chemin_du_fichier):
		try:
			with open(chemin_du_fichier, 'rb') as fichier:
				unpickler = pickle.Unpickler(fichier)
				contenu = unpickler.load()
		except FileNotFoundError:
			contenu = []
			self.write(chemin_du_fichier, contenu)
		return contenu
	
	def write(self, chemin_du_fichier, contenu):
		with open(chemin_du_fichier, 'wb') as fichier:
			pickler = pickle.Pickler(fichier)
			contenu = pickler.dump(contenu)
