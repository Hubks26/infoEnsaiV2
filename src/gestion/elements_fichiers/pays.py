from gestion.elements_fichiers.section import Section

class Pays(Section):
	"""Cette classe renvoie les différentes informations d'un pays contenu dans la base de données"""
	
	def __init__(self, num_pays, donnees):
		super().__init__(num_pays, donnees)
		
	def __lt__(self, autre_pays):
		return self.num_pays > autre_pays.num_pays

	def get_name(self):
		"""Cette méthode permet d'obtenir le nom du pays"""
		
		try:
			nom = self.contenu['Government']['Country name']['conventional short form']['text']
			if nom == 'none':
				raise KeyError
		except KeyError:
			try:
				nom = self.contenu['Government']['Country name']['conventional long form']['text']
			except KeyError:
				nom = None
		return nom

	def get_superficie(self):
		"""Cette méthode renvoie la superficie du pays"""
		
		try:
			superficie = self.contenu['Geography']['Area']['total']['text']
		except KeyError:
			superficie = 'NA'
		return superficie

	def get_pop(self):
		"""Cette méthode renvoie la population du pays"""
		
		try:
			pop = self.contenu['People and Society']['Population']['text']
		except KeyError:
			pop = 'NA'
		return pop

	def get_croissance_demo(self):
		"""Cette méthode renvoie la croissance démographique d'un pays"""
		
		try:
			croissance_demo = self.contenu['People and Society']['Population growth rate']['text']
		except KeyError:
			croissance_demo = 'NA'
		return croissance_demo

	def get_inflation(self):
		"""Cette méthode permet de renvoyer l'inflation du pays"""
		
		try:
			inflation = self.contenu['Economy']['Inflation rate (consumer prices)']['text']
		except KeyError:
			inflation = 'NA'
		return inflation

	def get_dette(self):
		"""Cette méthode permet de renvoyer la dette d'un pays"""
		
		try:
			dette = self.contenu['Economy']['Debt - external']['text']
		except KeyError:
			dette = 'NA'
		return dette

	def get_chomage(self):
		"""Cette méthode permet de renvoyer le taux de chômage d'un pays"""
		
		try:
			chomage = self.contenu['Economy']['Unemployment rate']['text']
		except KeyError:
			chomage = 'NA'
		return chomage

	def get_depenses_sante(self):
		"""Cette méthode permet de renvoyer le chiffre des dépenses d'un pays dans le domaine de la santé"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Health expenditures']['text']
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante

	def get_depenses_education(self):
		"""Cette méthode renvoie les dépenses d'un pays dans l'éducation"""
		
		try:
			depenses_education = self.contenu['People and Society']['Education expenditures']['text']
		except KeyError:
			depenses_education = 'NA'
		return depenses_education

	def get_depenses_militaires(self):
		"""Cette méthode renvoie les dépenses d'un pays dans le secteur militaire"""
		
		try:
			depenses_militaires = self.contenu['Military and Security']['Military expenditures']['text']
		except KeyError:
			depenses_militaires = 'NA'
		return depenses_militaires
	
	def get_classe_age1(self):
		"""Cette methode permet de regrouper les individus d'un âge entre 0 et 14 ans"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["0-14 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age2(self):
		"""Cette methode permet de regrouper les individus d'un âge entre 15 et 24 ans"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["15-24 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age3(self):
		"""Cette methode permet de regrouper les individus d'un âge entre 25 et 54 ans"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["25-54 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age4(self):
		"""Cette methode permet de regrouper les individus d'un âge entre 55 et 64 ans"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["55-64 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age5(self):
		"""Cette methode permet de regrouper les individus d'un âge entre 65 ans et plus"""
		
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["65 years and over"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_critere(self, critere):
		"""Cette méthode permet de renvoyer les différents résultats à fournir
		selon le critère du data scientist par les différentes méthodes de cette classe."""
		
		if critere == 'superficie':
			txt = self.get_superficie()
		elif critere == 'population':
			txt = self.get_pop()
		elif critere == 'croissance démographique':
			txt = self.get_croissance_demo()
		elif critere == 'inflation':
			txt = self.get_inflation()   
		elif critere == 'dette':
			txt = self.get_dette()
		elif critere == 'chômage':
			txt = self.get_chomage()
		elif critere == 'dépenses santé':
			txt = self.get_depenses_sante()
		elif critere == 'dépenses éducation':
			txt = self.get_depenses_education()
		elif critere == 'dépenses militaires':
			txt = self.get_depenses_militaires()
		elif critere == '0-14':	
			txt = self.get_classe_age1()
		elif critere == '15-24':
			txt = self.get_classe_age2()
		elif critere == '25-54':
			txt = self.get_classe_age3()
		elif critere == '55-64':
			txt = self.get_classe_age4()
		elif critere == '>=65':
			txt = self.get_classe_age5()
		else:
			raise KeyError
		return txt

	def set_name(self, nom_pays):
		"""Cette méthode permet de modifier le nom d'un pays dans la base de données"""
		
		self.contenu.update({'Government' : {'Country name' : {'conventional short form' : {'text' : nom_pays}, 'conventional long form' : {'text' : nom_pays}}}})

	def set_long_name(self, long_name):
		"""Cette méthode permet de modifier le nom d'un pays, mais en version longue"""
		
		self.contenu['Government']['Country name']['conventional long form'] = {'text' : long_name}

	def set_superficie(self, superficie):
		"""Cette méthode permet de modifier la superficie d'un pays dans la base de données"""
		
		self.contenu.update({'Geography' : {'Area' : {'total' : {'text' : superficie+' sq km'}}}})

	def set_pop(self, pop):
		"""Cette méthode permet de modifier la population d'un pays dans la base de données"""
		
		self.contenu.update({'People and Society' : {'Population' : {'text' : pop}}})

	def set_croissance_demo(self, croissance_demo):
		"""Cette méthode permet de modifier la croissance démographique d'un pays dans la base de données"""
		
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Population growth rate'] = {'text' : croissance_demo+'%'}
		else:
			self.contenu['People and Society'] = {'Population growth rate' : {'text' : croissance_demo+'%'}}
		
	def set_inflation(self, inflation):
		"""Cette méthode permet de modifier l'inflation d'un pays dans la base de données"""
		
		self.contenu.update({'Economy' : {'Inflation rate (consumer prices)' : {'text' : inflation+'%'}}})
		
	def set_dette(self, dette):
		"""Cette méthode permet de modifier la dette d'un pays dans la base de données"""
		
		if 'Economy' in self.contenu:
			self.contenu['Economy']['Debt - external'] = {'text' : '$'+dette}
		else:
			self.contenu['Economy'] = {'Debt - external' : {'text' : '$'+dette}}
		
	def set_chomage(self, chomage):
		"""Cette méthode permet de modifier le chômage d'un pays dans la base de données"""
		
		if 'Economy' in self.contenu:
			self.contenu['Economy']['Unemployment rate'] = {'text' : chomage+'%'}
		else:
			self.contenu['Economy'] = {'Unemployment rate' : {'text' : chomage+'%'}}
		
	def set_depenses_sante(self, depenses_sante):
		"""Cette méthode permet de modifier les dépenses dans le secteur de la santé d'un pays dans la base de données"""
		
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Health expenditures'] = {'text' : depenses_sante+'% of GDP'}
		else:
			self.contenu['People and Society'] = {'Health expenditures' : {'text' : depenses_sante+'% of GDP'}}
		
	def set_depenses_education(self, depenses_education):
		"""Cette méthode permet de modifier les dépenses dans l'éducation d'un pays dans la base de données"""
		
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Education expenditures'] = {'text' : depenses_education+'% of GDP'}
		else:
			self.contenu['People and Society'] = {'Education expenditures' : {'text' : depenses_education+'% of GDP'}}
		
	def set_depenses_militaires(self, depenses_militaires):
		"""Cette méthode permet de modifier les dépenses dans le secteur militaire d'un pays dans la base de données"""
		
		self.contenu.update({'Military and Security' : {'Military expenditures' : {'text' : depenses_militaires+'% of GDP'}}})

	def set_infos_de_base(self):
		"""Cette méthode permet d'ajouter des informations de base sur un pays, c'est-à-dire le nom du pays, 
		la superficie, sa population, sa croissance démographique, l'inflation, la dette, le chômage et les dépenses"""
		
		ajout_infos = input('\nVoulez vous ajouter des informations de base sur le pays (O/N) ?\n> ')
		if ajout_infos in ["o","O"]:
			long_name = input("\nEntrez la version longue du nom du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if long_name != "pass":
				self.set_long_name(long_name)
				input("\nVotre réponse a bien été enregistrée")
			superficie = input("\nEntrez la superficie (en sq km) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if superficie != "pass":
				self.set_superficie(superficie)
				input("\nVotre réponse a bien été enregistrée")
			pop = input("\nEntrez la population du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if pop != "pass":
				self.set_pop(pop)
				input("\nVotre réponse a bien été enregistrée")
			croissance_demo = input("\nEntrez le taux de croissance démographique (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if croissance_demo != "pass":
				self.set_croissance_demo(croissance_demo)
				input("\nVotre réponse a bien été enregistrée")
			inflation = input("\nEntrez le taux d'inflation (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if inflation != "pass":
				self.set_inflation(inflation)
				input("\nVotre réponse a bien été enregistrée")
			dette = input("\nEntrez la dette (en $) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if dette != "pass":
				self.set_dette(dette)
				input("\nVotre réponse a bien été enregistrée")
			chomage = input("\nEntrez le taux de chômage (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if chomage != "pass":
				self.set_chomage(chomage)
				input("\nVotre réponse a bien été enregistrée")
			depenses_sante = input("\nEntrez le taux de dépense en santé (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_sante != "pass":
				self.set_depenses_sante(depenses_sante)
				input("\nVotre réponse a bien été enregistrée")
			depenses_education = input("\nEntrez le taux de dépense en éducation (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_education != "pass":
				self.set_depenses_education(depenses_education)
				input("\nVotre réponse a bien été enregistrée")
			depenses_militaires = input("\nEntrez le taux de dépense militaires (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_militaires != "pass":
				self.set_depenses_militaires(depenses_militaires)
				input("\nVotre réponse a bien été enregistrée")
