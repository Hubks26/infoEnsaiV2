from acteurs.contributeur import Contributeur

class Geographe(Contributeur):
	def __init__(self):
		super().__init__()
		self.statut = 'géographe'
