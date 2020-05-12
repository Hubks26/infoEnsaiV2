
class Section:
	"""Cette classe permet de gérer des opérations élémentaires pour les sections"""
	
	def __init__(self, num_pays, donnees, chemin = []):
		"""Elle permet de créer une nouvelle section pour un pays"""
		
		assert num_pays <= len(donnees) and num_pays >= 0, "num_pays ne correspond à aucun pays de la base"
		
		contenu = donnees[num_pays]
		
		for nom_section in chemin:
			contenu = contenu[nom_section]
			
		self.contenu = contenu
		self.num_pays = num_pays
		self.chemin = chemin
		self.donnees = donnees
		
	def get_noms_sous_sections(self):
		"""Permet de retourner la liste des sections de la base de données"""
		
		noms_sous_sections = []
		for sous_section in self.contenu.keys():
			noms_sous_sections.append(sous_section)
		return noms_sous_sections
	
	def is_section_de_texte(self):
		"""Permet de savoir s'il y a un texte à afficher dans la section en question"""
		
		noms_sous_sections = self.get_noms_sous_sections()
		return 'text' in noms_sous_sections
