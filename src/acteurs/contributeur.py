from acteurs.consultant import Consultant

class Contributeur(Consultant):
	def __init__(self):
		super().__init__()
		self.is_connected = False
		self.statut = None
