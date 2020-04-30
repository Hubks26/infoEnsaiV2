from acteurs.individu import Individu
from gestion.elements_fichiers.proposition_correction import Proposition_Correction
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Consultant(Individu):
	# Cette classe hérite de la classe Individu. Il s'agit d'un acteur.
	# Le statut du consultant est "consultant"
	
	def __init__(self):
		super().__init__()
		self.statut = 'c'

	def correction(self, contenu, num_pays, donnees, chemin):
		# Cette méthode permet de proposer une correction.
		# Elle prend en argument un contenu et ne renvoie rien.
		# L'utilisateur n'a qu'à entrer la proposition de 
		# correction afin de l'enregistrer.
		
		if chemin[-1] == 'conventional short form' or chemin[-1] == 'conventional long form':
			input('\nVous ne pouvez pas proposer de correction pour le nom du pays.\nAppuyez sur entrer pour continuer.')
		else:
			rep = input('\nVoulez vous proposer une correction (O/N) ?\n> ')
			if rep in ['o', 'O']:
				while True:
					txt_correction = input('\nEntrez la proposition de correction :\n> ')
					if len(txt_correction) > 1:
						break
					print('\nVotre texte doit contenir au moins 1 caractère\n')
					
				prop_correction = Proposition_Correction(txt_correction, num_pays, chemin)
				gestionnaire = Gestionnaire()
				gestionnaire.save_elm(prop_correction)

				continuer = input('\nVotre proposition de correction a bien été enregistrée.\nAppuyez sur entrer pour continuer.')
