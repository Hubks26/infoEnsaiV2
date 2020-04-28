
class Section:
	def __init__(self, num_pays, donnees, chemin = []):
		
		assert num_pays <= len(donnees) and num_pays >= 0, "num_pays ne correspond à aucun pays de la base"
		
		contenu = donnees[num_pays]
		
		for nom_section in chemin:
			contenu = contenu[nom_section]
			
		self.contenu = contenu
		self.num_pays = num_pays
		self.chemin = chemin
		self.donnees = donnees
		
	def get_noms_sous_sections(self):
		noms_sous_sections = []
		for sous_section in self.contenu.keys():
			noms_sous_sections.append(sous_section)
		return noms_sous_sections
	
	def is_section_de_texte(self):
		noms_sous_sections = self.get_noms_sous_sections()
		return len(noms_sous_sections) == 1 and 'text' in noms_sous_sections
