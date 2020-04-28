from acteurs.geographe import Geographe
from acteurs.data_scientist import Data_Scientist

class Admin(Geographe, Data_Scientist):
	def __init__(self):
		super().__init__()
		self.statut = 'administrateur'
