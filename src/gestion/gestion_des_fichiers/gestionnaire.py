from gestion.gestion_des_fichiers.lecteur import Lecteur

class Gestionnaire(Lecteur):
	def save_elm(self, donnee):
		chemin = donnee.get_chemin_fichier()

		try:
			liste_elm = self.read(chemin)
		except FileNotFoundError:
			liste_elm = []
			self.write(chemin, liste_elm)

		liste_elm.append(donnee)

		self.write(chemin, liste_elm)
