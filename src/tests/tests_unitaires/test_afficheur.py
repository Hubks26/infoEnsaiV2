import unittest
from gestion.gestion_des_fichiers.afficheur import Afficheur

class TestAfficher(unittest.TestCase):
	
	def test_simplification(self):
		#Assume
		txt = 'This text is too long.'
		
		#Action
		afficheur = Afficheur()
		new_txt = afficheur.simplification(txt)
		
		expected_results = 'This text is too long...'
		
		#Assert
		self.assertEqual(new_txt, expected_results)
