import pandas
from gestion.gestion_des_fichiers.afficheur import Afficheur
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.pays import Pays

class Resume(Afficheur):
	
	def table_criteres(self, liste_pays_a_afficher):
		noms_pays = [self.simplification(pays.get_name()) for pays in liste_pays_a_afficher]
		
		criteres = ['Superficie', 'Population', 'Croissance démographique', 'Inflation', 'Dette', 'Taux de chômage', 'Taux de dépenses en santé', 'Taux de dépenses en éducation', 'Taux de dépenses militaires']
		
		valeurs_pays = [[self.simplification(pays.get_superficie()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_pop()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_croissance_demo()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_inflation()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_dette()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_chomage()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_depenses_sante()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_depenses_education()) for pays in liste_pays_a_afficher],
						[self.simplification(pays.get_depenses_militaires()) for pays in liste_pays_a_afficher]]
		
		return pandas.DataFrame(valeurs_pays, index = criteres, columns = noms_pays)
	
	def top_and_flop(self, critere, taille_classement):
		donnees = Data_Base().donnees
		
		liste_triee_selon_critere = self._liste_triee_selon_critere(donnees, critere)
		
		top = []
		flop = []
		rang_top = range(1,n+1)
		rang_flop = [len(liste_triee_selon_critere)-i for i in range(n)]
		col = ['PAYS', critere.upper()]
		for i in range(n):
				top.append([liste_triee_selon_critere[-i-1][1].get_name(), self.simplification(liste_triee_selon_critere[-i-1][1].get_critere(critere))])
				flop.append([liste_triee_selon_critere[i][1].get_name(), self.simplification(liste_triee_selon_critere[i][1].get_critere(critere))])

		return (pandas.DataFrame(top, index = rang_top, columns = col), pandas.DataFrame(flop, index = rang_flop, columns = col))
	
	def sup_inf_seuil(self, critere, seuil):
		donnees = Data_Base().donnees
		
		liste_triee_selon_critere = self._liste_triee_selon_critere(donnees, critere)
		liste_triee_selon_critere.reverse()
		pays_sup_seuil = []
		pays_inf_seuil = []
		col = ['PAYS', critere.upper()]
		
		for elm in liste_triee_selon_critere:
			if elm[0] >= seuil:
				pays_sup_seuil.append([elm[1].get_name(), self.simplification(elm[1].get_critere(critere))])
			else :
				pays_inf_seuil.append([elm[1].get_name(), self.simplification(elm[1].get_critere(critere))])
		
		tableau_pays_sup = pandas.DataFrame(pays_sup_seuil, index=[i+1 for i in range(len(pays_sup_seuil))], columns=col)
		tableau_pays_inf = pandas.DataFrame(pays_inf_seuil, index=[i+1 for i in range(len(pays_inf_seuil))], columns=col)
		
		return (len(pays_sup_seuil), tableau_pays_sup, len(pays_inf_seuil), tableau_pays_inf) 

	def _liste_triee_selon_critere(self, donnees, critere):
		liste = []
		for num_pays in range(len(donnees)):
			pays = Pays(num_pays, donnees)
			if pays.get_name() and self.numerisation_critere(pays, critere) != 'NA':
				liste.append((self.numerisation_critere(pays, critere), pays))
		liste.sort()
		return liste
