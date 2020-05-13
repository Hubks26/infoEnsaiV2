from affichage.menu_ouvert import Menu_Ouvert
from acteurs.contributeur import Contributeur
from gestion.elements_fichiers.data_base import Data_Base
from gestion.elements_fichiers.pays import Pays
from gestion.gestion_des_fichiers.resume import Resume
from gestion.gestion_des_fichiers.graphique import Graphique

class Data_Scientist(Contributeur):
	"""Cette classe correspond au Data Scientist"""
	
	def __init__(self):
		"""Son statut est la lettre 'd'"""
		
		super().__init__()
		self.statut = 'd'
		
	def resume_stat(self, contenu):
		"""Cette méthode est la tâche résumé d'informations. Elle affiche plusieurs tâches que peut effectuer
		le data scientist et renverra le résultat par la méthode correspondante au choix de la tâche.
		Ele prend en compte le contenu que ce que veut l'administrateur."""
		
		if self.verification_connexion():
			if self.contenu_initial == {}:
				self.contenu_initial = contenu
			
			choix_resume = {}
			choix_resume["question"] = "Choisissez une option d'affichage."
			choix_resume["individu"] = contenu["individu"]
			choix_resume["pseudo"] = contenu["pseudo"]
			choix_resume["options"] = [
				"Afficher les critères usuels d'un ou plusieurs pays",
				"Afficher les premiers/derniers pays selon un certain critère", 
				"Afficher les pays dont un critère dépasse un certain seuil",
				"Afficher le tableau des classes d'âge pour certains pays",
				"Afficher la somme des critères cumulables",
				"Afficher le summary d'un critère",
				"Afficher les différents profils de pays"]
			choix_resume['options basiques'] = [["RETOUR AU MENU DE L'ACTEUR", 'R'], ["QUITTER", 'Q']]
			choix_resume["actions"] = [
				lambda var : self.criteres_usuels(contenu), 
				lambda var : self.top_flop(contenu), 
				lambda var : self.resume_seuil(contenu), 
				lambda var : self.classes_age(contenu),
				lambda var : self.somme(contenu),
				lambda var : self.summary(contenu),
				lambda var : self.profils_pays(contenu),
				lambda var : Menu_Ouvert(self.contenu_initial), 
				self.quitter]
			return Menu_Ouvert(choix_resume)
		else:
			return Menu_Ouvert(contenu)
		
	def representation_graphique(self, contenu):
		"""Cette méthode fonctionne de la même façon que la méthode resume_stat.
		Le data scientist à le choix d'afficher un diagramme en barre ou une boite à moustache."""
		
		if self.verification_connexion():
			if self.contenu_initial == {}:
				self.contenu_initial = contenu
			
			choix_representaion = {}
			choix_representaion["question"] = "Choisissez le type de graphique."
			choix_representaion["individu"] = contenu["individu"]
			choix_representaion['pseudo'] = contenu['pseudo']
			choix_representaion["options"] = ["Diagramme en barres", "Boîte à moustache"]
			choix_representaion['options basiques'] = [["RETOUR AU MENU DE L'ACTEUR", 'R'], ["QUITTER", 'Q']]
			choix_representaion["actions"] = [
				lambda var : self.diag_barres(contenu),
				lambda var : self.box_plot(contenu),
				lambda var : Menu_Ouvert(self.contenu_initial),
				self.quitter]
			return Menu_Ouvert(choix_representaion)
		else :
			return Menu_Ouvert(contenu)
		
	def criteres_usuels(self, contenu, liste_pays_a_afficher = []):
		"""Cette fonction permet au data scientist d'avoir le choix entre ajouter un pays, supprimer un pays d'une
		liste ou bien de faire un résumé d'information de cette même liste."""
		
		resume = Resume()
		if len(liste_pays_a_afficher) == 0:
			return self._ajout_pays_table_criteres(contenu, liste_pays_a_afficher, self.criteres_usuels)
		
		contenu_menu_criteres = {}
		contenu_menu_criteres['individu'] = contenu['individu']
		contenu_menu_criteres['pseudo'] = contenu['pseudo']
		contenu_menu_criteres['question'] = resume.table_criteres(liste_pays_a_afficher)
		contenu_menu_criteres["options"] = ["Ajouter un pays à la table", "Retirer un pays de la table"]
		contenu_menu_criteres['options basiques'] = [
			["RETOUR", 'R'],
			["RETOUR AU MENU DE L'ACTEUR", 'RMA'],
			["QUITTER", 'Q']]
		contenu_menu_criteres["actions"] = [
			lambda var : self._ajout_pays_table_criteres(var, liste_pays_a_afficher, self.criteres_usuels),
			lambda var : self._retrait_pays_table_criteres(var, liste_pays_a_afficher, self.criteres_usuels),
			lambda var : self.resume_stat(var),
			lambda var : Menu_Ouvert(self.contenu_initial),
			self.quitter]
		return Menu_Ouvert(contenu_menu_criteres)
	
	def top_flop(self, contenu, critere=None):
		"""Cette méthode permet d'afficher les premiers et les derniers pays selon un certain critère."""
		
		resume = Resume()
		if not critere:
			return self._choix_critere(contenu, self.top_flop)
		else :
			print('\nLe critère choisi est {}.'.format(critere.upper()))
			
		print('Entrez la taille du classement (entre 5 et 50) :\n')
		while True:
			n = input('> ')
			try :
				n = int(n)
			except ValueError :
				print('\nVeuillez entrer un entier.\n')
				continue
			if n < 5 or n > 50:
				print('\nLa taille du classement doit être entre 5 et 50.\n')
				continue
			print('')
			break
		
		top, flop = resume.top_and_flop(critere, n)
		
		print("\nTop selon le critère : {}\n".format(critere.upper()))
		print(top)
		print("\n\nFlop selon le critère : {}\n".format(critere.upper()))
		print(flop)
		input("\nAppuyez sur entrer pour continuer.")
		return self.top_flop(contenu)
	
	def resume_seuil(self, contenu, critere=None):
		"""Afficher les pays dont un critère dépasse un certain seuil"""
		
		resume = Resume()
		if not critere:
			return self._choix_critere(contenu, self.resume_seuil)
		else :
			print('\nLe critère choisi est {}.'.format(critere.upper()))
			
		if critere == 'superficie':
			seuil = print("Entrez le seuil (en sq km) que vous voulez :\n")
		if critere == 'population':
			seuil = print("Entrez le seuil (en nombre d'habitant) que vous voulez :\n")
		if critere in ['croissance démographique', 'inflation', 'chômage', ]:
			seuil = print("Entrez le seuil (en %) que vous voulez :\n")
		if critere == 'dette':
			seuil = print("Entrez le seuil (en %) que vous voulez :\n")
		if critere in ['dépenses santé', 'dépenses education', 'dépenses militaires']:
			seuil = print("Entrez le seuil (en % of GDP) que vous voulez :\n")
	
		while True:
			seuil = input('> ')
			try :
				seuil = float(seuil)
			except ValueError :
				print('\nLa réponse attendue doit être un nombre.\n')
				continue
			break
		
		nb_pays_sup_seuil, tableau_pays_sup, nb_pays_inf_seuil, tableau_pays_inf = resume.sup_inf_seuil(critere, seuil)
		
		if nb_pays_sup_seuil == 0:
			print("\nIl n'existe aucun pays qui dépasse ce seuil.")
		else:
			print("\nVoici les pays qui dépassent ce seuil :\n")
			print(tableau_pays_sup)
				
		if nb_pays_inf_seuil == 0:
			print("\nIl n'existe aucun pays en dessous de ce seuil.")
		else:
			input("\nAppuyez sur entrer pour afficher les pays en dessous de ce seuil.")
			print("\nVoici les pays en dessous de ce seuil :\n")
			print(tableau_pays_inf)
				
		input("\nAppuyez sur entrer pour continuer.")
		return self.resume_seuil(contenu)
	
	def classes_age(self, contenu, liste_pays_a_afficher=[]):
		"""Afficher le tableau des classes d'âge pour certains pays"""
		
		resume = Resume()
		if len(liste_pays_a_afficher) == 0:
			return self._ajout_pays_table_criteres(contenu, liste_pays_a_afficher, self.classes_age)
		
		contenu_menu_classes_age = {}
		contenu_menu_classes_age['individu'] = contenu['individu']
		contenu_menu_classes_age['pseudo'] = contenu['pseudo']
		contenu_menu_classes_age['question'] = resume.tableau_classes_age(liste_pays_a_afficher)
		contenu_menu_classes_age["options"] = ["Ajouter un pays à la table", "Retirer un pays de la table"]
		contenu_menu_classes_age['options basiques'] = [
			["RETOUR", 'R'],
			["RETOUR AU MENU DE L'ACTEUR", 'RMA'],
			["QUITTER", 'Q']]
		contenu_menu_classes_age["actions"] = [
			lambda var : self._ajout_pays_table_criteres(var, liste_pays_a_afficher, self.classes_age),
			lambda var : self._retrait_pays_table_criteres(var, liste_pays_a_afficher, self.classes_age),
			lambda var : self.resume_stat(var),
			lambda var : Menu_Ouvert(self.contenu_initial),
			self.quitter]
		
		return Menu_Ouvert(contenu_menu_classes_age)
	
	def somme(self, contenu, critere=None):
		"""Afficher la somme des critères cumulables"""
		
		resume = Resume()
		print(resume.somme())
		input("\nAppuyez sur entrer pour continuer.")
		return self.resume_stat(contenu)
	
	def summary(self, contenu, critere=None):
		"""Afficher le summary d'un critère"""
		
		resume = Resume()
		print('')
		print(resume.summary())
		input("\nAppuyez sur entrer pour continuer.")
		return self.resume_stat(contenu)
	
	def profils_pays(self, contenu):
		"""Afficher les différents profils de pays"""
		
		resume = Resume()
		while True:
			nb_cluster = input('\nEntrez le nombre de clusters que vous désirez (entre 3 et 10)\n> ')
			try :
				nb_cluster = int(nb_cluster)
			except ValueError:
				print('\nVeuillez entrer un entier')
				continue
			if 3 > nb_cluster or nb_cluster > 10:
				print('\nLe nombre de clusters doit être compris entre 3 et 10')
				continue
			break
		
		print('')
		print(resume.clustering(nb_cluster))
		input("\nAppuyez sur entrer pour continuer.")
		return self.resume_stat(contenu)
	
	def diag_barres(self, contenu, critere=None):
		"""Cette méthode permet de retourner le diagramme en barres selon un critère"""
		
		graphique = Graphique()
		if not critere:
			return self._choix_critere(contenu, self.diag_barres, graphique=True)
		else :
			print('\nLe critère choisi est {}.'.format(critere.upper()))
		
		input("Appuyez sur entrer pour afficher le diagramme.")
		graphique.diagramme_en_barres(critere)
		input("\nAppuyez sur entrer pour continuer.")
		return self.diag_barres(contenu)
	
	def box_plot(self, contenu):
		"""Cette méthode permet de renvoyer les boites à moustaches"""
		
		graphique = Graphique()
		
		input("\nAppuyez sur entrer pour afficher le diagramme.")
		graphique.boites_a_moustache()
		input("\nAppuyez sur entrer pour continuer.")
		return self.representation_graphique(contenu)
	
	def _ajout_pays_table_criteres(self,contenu, liste_pays_a_afficher, fonction_a_appliquer):
		"""Cette méthode permet d'ajouter un pays à une liste afin d'appliquer une autre méthode 
		en fonction d'un certain critère. Cette méthode est utilisé par la fonction critere_usuel."""
		
		donnees = Data_Base().donnees
		nb_pays = len(donnees)
		
		if len(liste_pays_a_afficher) >= 10:
			input("\nVous ne pouvez pas afficher plus de 10 pays à la fois.\nAppuyez sur entrer pour continuer.")
			return fonction_a_appliquer(contenu, liste_pays_a_afficher)
		
		choix_pays = {}
		choix_pays['question'] = 'Choisissez un pays.'
		choix_pays['individu'] = contenu['individu']
		choix_pays['pseudo'] = contenu['pseudo']
		
		liste_des_pays = []
		liste_des_nums_pays_a_afficher = [pays.num_pays for pays in liste_pays_a_afficher]
		liste_des_noms_pays_a_afficher = [pays.get_name() for pays in liste_pays_a_afficher]
		
		for num_pays in range(nb_pays):
			nom_pays = Pays(num_pays, donnees).get_name()
			if nom_pays and nom_pays not in liste_des_noms_pays_a_afficher:
				liste_des_pays.append((nom_pays, num_pays))
		liste_des_pays.sort()
		liste_des_noms = [pays[0] for pays in liste_des_pays]
		liste_des_nums = [pays[1] for pays in liste_des_pays]
		
		choix_pays['options'] = liste_des_noms
		choix_pays['options basiques'] = []
		choix_pays['actions'] = [lambda var, num=num : fonction_a_appliquer(contenu, liste_pays_a_afficher+[Pays(num, donnees)]) for num in liste_des_nums if num not in liste_des_nums_pays_a_afficher]
		
		return Menu_Ouvert(choix_pays)

	def _retrait_pays_table_criteres(self,contenu, liste_pays_a_afficher, fonction_a_appliquer):
		"""Cette méthode permet de retirer un pays d'une liste.  
		Cette méthode est utilisé par la fonction critere_usuel."""
		
		if len(liste_pays_a_afficher) == 1:
			input("\nIl doit y avoir au moins un pays dans la table.\nAppuyez sur entrer pour continuer.")
			return fonction_a_appliquer(contenu, liste_pays_a_afficher)
		
		choix_pays = {}
		choix_pays['question'] = 'Choisissez un pays à retirer de la table.'
		choix_pays['individu'] = contenu['individu']
		choix_pays['pseudo'] = contenu['pseudo']
		
		choix_pays['options'] = [pays.get_name() for pays in liste_pays_a_afficher]
		choix_pays['options basiques'] = []
		
		choix_pays['actions'] = [lambda var, i=i : fonction_a_appliquer(contenu, liste_pays_a_afficher[:i]+liste_pays_a_afficher[i+1:]) for i in range(len(liste_pays_a_afficher))]
		
		return Menu_Ouvert(choix_pays)
	
	def _choix_critere(self, contenu, fonction_a_appliquer, graphique=False):
		"""Cette méthode permet à l'utilisateur de choisir un critère sur les pays qu'il aura selectionné
		dans la liste crée au préalable."""
		
		criteres = ['Superficie', 'Population', 'Croissance démographique', 'Inflation', 'Dette', 'Taux de chômage', 'Taux de dépenses en santé', 'Taux de dépenses en éducation', 'Taux de dépenses militaires']
		
		return_function = lambda var : self.resume_stat(var)
		if graphique:
			return_function = lambda var : self.representation_graphique(var)
		
		choix_critere = {}
		choix_critere["question"] = "Choisissez un critère."
		choix_critere["individu"] = contenu["individu"]
		choix_critere['pseudo'] = contenu['pseudo']
		choix_critere["options"] = criteres
		choix_critere['options basiques'] = [['RETOUR', 'R'], ["RETOUR AU MENU DE L'ACTEUR", 'RMA'], ["QUITTER", 'Q']]
		choix_critere["actions"] = [
			lambda var : fonction_a_appliquer(contenu, 'superficie'),
			lambda var : fonction_a_appliquer(contenu, 'population'),
			lambda var : fonction_a_appliquer(contenu, 'croissance démographique'),
			lambda var : fonction_a_appliquer(contenu, 'inflation'),
			lambda var : fonction_a_appliquer(contenu, 'dette'),
			lambda var : fonction_a_appliquer(contenu, 'chômage'),
			lambda var : fonction_a_appliquer(contenu, 'dépenses santé'),
			lambda var : fonction_a_appliquer(contenu, 'dépenses éducation'),
			lambda var : fonction_a_appliquer(contenu, 'dépenses militaires'),
			return_function,
			lambda var : Menu_Ouvert(self.contenu_initial),
			self.quitter]
		
		return Menu_Ouvert(choix_critere)
