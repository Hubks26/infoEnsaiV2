import unittest
from gestion.elements_fichiers.section import Section

class TestSection(unittest.TestCase):
	
	data_base = [{'Introduction' : {'Background' : {'text' : 'Texte de la section'}},
					'Government' : {'Country name' : {'conventional short form' : {'text' : 'France'}}}},
					{'Introduction' : {'Background' : {'text' : 'Texte de la section'}},
					'Government' : {'Country name' : {'conventional short form' : {'text' : 'Espagne'}}}},
					{'Introduction' : {'Background' : {'text' : 'Texte de la section'}},
					'Government' : {'Country name' : {'conventional short form' : {'text' : 'Italy'}}}}]
	
	def test_get_noms_sous_sections(self):
		#Assume
		donnees = self.data_base
		
		#Action
		section = Section(0, donnees)
		liste_des_sous_sections = section.get_noms_sous_sections()
		expected_results = ['Introduction', 'Government']
		
		#Assert
		self.assertEqual(liste_des_sous_sections, expected_results)
		
	def test_is_section_de_texte(self):
		#Assume
		donnees = self.data_base
		
		#Action
		section = Section(0, donnees, ['Introduction', 'Background'])
		is_section_de_texte = section.is_section_de_texte()
		expected_results = True
		
		#Assert
		self.assertEqual(is_section_de_texte, expected_results)
