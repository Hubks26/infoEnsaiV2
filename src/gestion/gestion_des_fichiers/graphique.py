import matplotlib.pyplot as plt
from gestion.gestion_des_fichiers.afficheur import Afficheur
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.pays import Pays

class Graphique(Afficheur):
	"""Cette classe permet de créer les graphiques : les diagrammes en barres et les boites à moustaches"""

	def diagramme_en_barres(self, critere):
		"""Cette méthode crée un diagramme en barres selon un critère choisi par le data scientist"""
		
		donnees = Data_Base().donnees
		liste_triee_selon_critere = self.liste_triee_selon_critere(donnees, critere)
		liste_triee = [elm[0] for elm in liste_triee_selon_critere]
		x = [self.simplification(elm[1].get_name()) for elm in liste_triee_selon_critere]
		plt.barh(x, liste_triee, color='b')
		plt.yticks(fontsize=3.2)
		plt.show()
		
	def boites_a_moustache(self):
		"""Cette méthode crée une boîte à moustache sur les différentes classes d'ages."""
		
		donnees = Data_Base().donnees
		
		classe_age_0 = []
		classe_age_1 = []
		classe_age_2 = []
		classe_age_3 = []
		classe_age_4 = []
		
		for num_pays in range(len(donnees)):
			pays = Pays(num_pays, donnees)
			if pays.get_name():
				if self.numerisation_critere(pays, '0-14') != 'NA':
					classe_age_0.append(self.numerisation_critere(pays, '0-14'))
				if self.numerisation_critere(pays, '15-24') != 'NA':
					classe_age_1.append(self.numerisation_critere(pays, '15-24'))
				if self.numerisation_critere(pays, '25-54') != 'NA':
					classe_age_2.append(self.numerisation_critere(pays, '25-54'))
				if self.numerisation_critere(pays, '55-64') != 'NA':
					classe_age_3.append(self.numerisation_critere(pays, '55-64'))
				if self.numerisation_critere(pays, '>=65') != 'NA':
					classe_age_4.append(self.numerisation_critere(pays, '>=65'))
					
		plt.title("Box-plots correspondants aux répartitions des valeurs des 5 classes d’âge pour tous les pays.")
		plt.boxplot([classe_age_0, classe_age_1, classe_age_2, classe_age_3, classe_age_4], labels = ["0-14 years","15-24 years","25-54 years","55-64 years",">=65"])
		plt.show()
