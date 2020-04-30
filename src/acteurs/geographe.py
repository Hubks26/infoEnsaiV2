from acteurs.contributeur import Contributeur
from gestion.elements_fichiers.section import Section
from gestion.gestion_des_fichiers.gestionnaire import Gestionnaire

class Geographe(Contributeur):
	def __init__(self):
		super().__init__()
		self.statut = 'g'
		
	def correction(self, contenu, num_pays, donnees, chemin):
		section_de_texte = Section(num_pays, donnees, chemin)
		gestionnaire = Gestionnaire()
		
		if chemin[-1] == 'conventional short form' or chemin[-1] == 'conventional long form':
			input('\nVous ne pouvez pas modifier le nom du pays.\nAppuyez sur entrer pour continuer.')
		else:
			rep = input('\nVoulez vous modifier le texte (O/N) ?\n> ')
			if rep in ['o', 'O']:
				if self.verification_connexion():
					while True:
						txt_correction = input('\nEntrez le nouveau texte :\n> ')
						if len(txt_correction) > 1:
							break
						print('\nVotre texte doit contenir au moins 1 caractère\n')
						
					section_de_texte.contenu['text'] = txt_correction
					
					confirmation = input("\nConfirmation de la modification #Cela écrasera le texte initial# (O/N) ?\n> ")
					if confirmation in ["o","O"]:
						gestionnaire.update(section_de_texte)
						input('\nVotre modification a bien été enregistrée.\nAppuyez sur entrer pour continuer.')
					else :
						input("\nVotre tentative de modification n'a pas abouti.\nAppuyez sur entrer pour continuer.")
