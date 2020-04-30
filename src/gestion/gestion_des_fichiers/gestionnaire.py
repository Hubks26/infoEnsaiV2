import json
from gestion.gestion_des_fichiers.lecteur import Lecteur

file_name = "data.json"
directory_data = "../media/files/"

class Gestionnaire(Lecteur):
	def save_elm(self, elm):
		chemin = elm.get_chemin_fichier()
		liste_elm = self.read(chemin)
		liste_elm.append(elm)
		self.write(chemin, liste_elm)
		
	def suppr_elm(self, elm_a_supprimer):
		chemin = elm_a_supprimer.get_chemin_fichier()
		liste_elm = self.read(chemin)
		nouvelle_liste_elm = []
		
		for elm in liste_elm:
			if elm != elm_a_supprimer:
				nouvelle_liste_elm.append(elm)
		if len(nouvelle_liste_elm) == len(liste_elm):
			input('\nEchec de la suppression. Aucun élément ne correspond à votre entrée.\nAppuyez sur entrer pour continuer.\n')
		else :
			confirmation = input('\nConfirmation de la suppression du compte (O/N) ?\n> ')
			if confirmation in ['o', 'O']:
				self.write(chemin, nouvelle_liste_elm)
				input('\nLa suppression a bien été effectuée\nAppuyez sur entrer pour continuer')
			else :
				input('\nEchec de la suppression.\nAppuyez sur entrer pour continuer.\n')
				
	def update(self, section):
		donnees = section.donnees
		with open(directory_data + file_name, "w") as json_file:
			json.dump(donnees, json_file)
