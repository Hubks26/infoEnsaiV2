import json
from gestion.elements_fichiers.elm_fichier import Elm_Fichier

class Data_Base(Elm_Fichier):
	def __init__(self):
		super().__init__("data.json")
		
		with open(self.get_chemin_fichier()) as json_file:
			donnees = json.load(json_file)
		self.donnees = donnees
