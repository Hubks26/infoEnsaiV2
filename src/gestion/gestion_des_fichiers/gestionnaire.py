import json
from gestion.gestion_des_fichiers.lecteur import Lecteur

file_name = "data.json"
directory_data = "../media/files/"

class Gestionnaire(Lecteur):
	"""Cette classe configure les méthodes permettant la modification de la base de données"""
	
	def save_elm(self, elm):
		"""méthode permettant d'ajouter un élément à la base de données"""
		
		chemin = elm.get_chemin_fichier()
		liste_elm = self.read(chemin)
		liste_elm.append(elm)
		self.write(chemin, liste_elm)
		
	def suppr_elm(self, elm_a_supprimer):
		"""méthode permettant de supprimer un élément de la base de données"""
		
		chemin = elm_a_supprimer.get_chemin_fichier()
		liste_elm = self.read(chemin)
		nouvelle_liste_elm = []
		
		for elm in liste_elm:
			if elm != elm_a_supprimer:
				nouvelle_liste_elm.append(elm)
				
		self.write(chemin, nouvelle_liste_elm)
				
	def update(self, donnees):
		"""méthode permettant de mettre à jour le fichier"""
		
		with open(directory_data + file_name, "w") as json_file:
			json.dump(donnees, json_file)
