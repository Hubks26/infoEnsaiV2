from gestion.elements_fichiers.section import Section

class Pays(Section):
	def __init__(self, num_pays, donnees):
		super().__init__(num_pays, donnees)

	def get_name(self):
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
		try:
			superficie = self.contenu['Geography']['Area']['total']['text']
		except KeyError:
			superficie = 'Na'
		return superficie

	def get_pop(self):
		try:
			pop = self.contenu['People and Society']['Population']['text']
		except KeyError:
			pop = 'Na'
		return pop

	def get_croissance_demo(self):
		try:
			croissance_demo = self.contenu['People and Society']['Population growth rate']['text']
		except KeyError:
			croissance_demo = 'Na'
		return croissance_demo

	def get_inflation(self):
		try:
			inflation = self.contenu['Economy']['Inflation rate (consumer prices)']['text']
		except KeyError:
			inflation = 'Na'
		return inflation

	def get_dette(self):
		try:
			dette = self.contenu['Economy']['Debt - external']['text']
		except KeyError:
			dette = 'Na'
		return dette

	def get_chomage(self):
		try:
			chomage = self.contenu['Economy']['Unemployment rate']['text']
		except KeyError:
			chomage = 'Na'
		return chomage

	def get_depenses_sante(self):
		try:
			depenses_sante = self.contenu['People and Society']['Health expenditures']['text']
		except KeyError:
			depenses_sante = 'Na'
		return depenses_sante

	def get_depenses_education(self):
		try:
			depenses_education = self.contenu['People and Society']['Education expenditures']['text']
		except KeyError:
			depenses_education = 'Na'
		return depenses_education
	
	def get_depenses_militaires(self):
		try:
			depenses_militaires = self.contenu['Military and Security']['Military expenditures']['text']
		except KeyError:
			depenses_militaires = 'Na'
		return depenses_militaires
