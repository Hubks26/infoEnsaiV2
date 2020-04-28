import pickle

class Lecteur:
	def __init__(self):
		pass
	
	def read(self, chemin_du_fichier):
		with open(chemin_du_fichier, 'rb') as fichier:
			unpickler = pickle.Unpickler(fichier)
			contenu = unpickler.load()
			
		return contenu
	
	def write(self, chemin_du_fichier, contenu):
		with open(chemin_du_fichier, 'wb') as fichier:
			pickler = pickle.Pickler(fichier)
			contenu = pickler.dump(contenu)
