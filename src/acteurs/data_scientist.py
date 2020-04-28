from acteurs.contributeur import Contributeur

class Data_Scientist(Contributeur):
	def __init__(self):
		super().__init__()
		self.statut = 'data_scientist'
