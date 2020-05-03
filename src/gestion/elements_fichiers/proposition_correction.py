from gestion.elements_fichiers.elm_fichier import Elm_Fichier
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.pays import Pays

class Proposition_Correction(Elm_Fichier):
	def __init__(self, txt_prop, num_pays, chemin_prop):
		super().__init__("props_corrections")
		self.txt_prop = txt_prop
		self.num_pays = num_pays
		self.chemin_prop = chemin_prop

	def __str__(self):
		donnees = Data_Base().donnees
		res = Pays(self.num_pays, donnees).get_name() + '/'
		for i in range(len(self.chemin_prop)):
			res += self.chemin_prop[i] + '/'
		return res
	
	def __eq__(self, autre_proposition):
		return self.txt_prop == autre_proposition.txt_prop and self.chemin_prop == autre_proposition.chemin_prop
