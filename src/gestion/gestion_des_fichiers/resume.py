import pandas
import numpy as np
from sklearn.cluster import KMeans
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
		
		liste_triee_selon_critere = self.liste_triee_selon_critere(donnees, critere)
		
		top = []
		flop = []
		rang_top = range(1,taille_classement+1)
		rang_flop = [len(liste_triee_selon_critere)-i for i in range(taille_classement)]
		col = ['PAYS', critere.upper()]
		for i in range(taille_classement):
				top.append([liste_triee_selon_critere[-i-1][1].get_name(), self.simplification(liste_triee_selon_critere[-i-1][1].get_critere(critere))])
				flop.append([liste_triee_selon_critere[i][1].get_name(), self.simplification(liste_triee_selon_critere[i][1].get_critere(critere))])

		return (pandas.DataFrame(top, index = rang_top, columns = col), pandas.DataFrame(flop, index = rang_flop, columns = col))
	
	def sup_inf_seuil(self, critere, seuil):
		donnees = Data_Base().donnees
		
		liste_triee_selon_critere = self.liste_triee_selon_critere(donnees, critere)
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

	def tableau_classes_age(self, liste_pays_a_afficher):
		noms_pays = [self.simplification(pays.get_name()) for pays in liste_pays_a_afficher]
		
		criteres = ["0-14", "15-24", "25-54", "55-64", ">= 65"]
		
		valeurs_classes_age = [[self.simplification(pays.get_classe_age1()) for pays in liste_pays_a_afficher],
							[self.simplification(pays.get_classe_age2()) for pays in liste_pays_a_afficher],
							[self.simplification(pays.get_classe_age3()) for pays in liste_pays_a_afficher],
							[self.simplification(pays.get_classe_age4()) for pays in liste_pays_a_afficher],
							[self.simplification(pays.get_classe_age5()) for pays in liste_pays_a_afficher]]
		
		return pandas.DataFrame(valeurs_classes_age, index = criteres, columns = noms_pays)
	
	def somme(self):
		donnees = Data_Base().donnees
		superficie_tot = sum([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'superficie')])
		population_tot = sum([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'population')])
		dette_tot = sum([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'dette')])
		
		criteres = ["La somme des superficies de tous les pays", "La somme des populations de tous les pays", "La somme des dettes de tous les pays"]
		index = criteres
		valeurs = [[superficie_tot],[population_tot],[dette_tot]]
		return pandas.DataFrame(valeurs, index = criteres, columns = [''])
		
	def summary(self):
		donnees = Data_Base().donnees
		
		superficie = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'superficie')])
		population = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'population')])
		croissance_demographique = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'croissance démographique')])
		inflation = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'inflation')])
		dette = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'dette')])
		chomage = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'chômage')])
		depenses_sante = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'dépenses santé')])
		depenses_éducation = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'dépenses éducation')])
		depenses_militaires = pandas.Series([elm[0] for elm in self.liste_triee_selon_critere(donnees, 'dépenses militaires')])
		
		dic = {'Superficie' : superficie,
			'Population' : population,
			'Croissance démo' : croissance_demographique,
			'Inflation' : inflation,
			'Dette' : dette,
			'Chômage' : chomage,
			'Dépenses santé' : depenses_sante,
			'Dépenses éducation' : depenses_éducation,
			'Dépenses militaires' : depenses_militaires}
		
		return pandas.DataFrame(dic).describe()
	
	def clustering(self, nb_clusters):
		donnees = Data_Base().donnees
		
		criteres = ['superficie', 'population', 'croissance démographique', 'inflation', 'dette', 'chômage', 'dépenses santé', 'dépenses éducation', 'dépenses militaires']
		
		valeurs_pays = []
		liste_des_pays_comptabilises = []
		
		for num_pays in range(len(donnees)):
			pays = Pays(num_pays, donnees)
			if pays.get_name():
				if True not in [self.numerisation_critere(pays, critere) == 'NA' for critere in criteres]:
					liste_des_pays_comptabilises.append(self.simplification(pays.get_name()))
					valeurs_pays.append([self.numerisation_critere(pays, critere) for critere in criteres])
		
		clf = KMeans(n_clusters=nb_clusters)
		clf.fit(np.array(valeurs_pays))
		labels = clf.labels_
		
		pays_dans_clusters = [[] for i in range(nb_clusters)]
		
		for i in range(len(labels)):
			for cl in range(nb_clusters):
				if labels[i] == cl:
					pays_dans_clusters[cl].append(liste_des_pays_comptabilises[i])
		
		for cluster in pays_dans_clusters:
			while len(cluster) < max([len(cl) for cl in pays_dans_clusters]):
				cluster.append('')

		liste_des_clusters = ['Cluster {}'.format(i+1) for i in range(nb_clusters)]

		return pandas.DataFrame(pays_dans_clusters, index = liste_des_clusters).T
		
		
