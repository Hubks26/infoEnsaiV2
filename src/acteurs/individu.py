from affichage.menu_ouvert import Menu_Ouvert
from affichage.menu_ferme import Menu_Ferme

class Individu:
	# Classe mère des différents acteurs
	
	def __init__(self):
		self.statut = None
		self.contenu_initial = {}
		
	def quitter(self, contenu):
		# Cette méthode est commune à tous les individus. Elle prend en argument
		# un contenu de menu (dict) et renvoie un menu ouvert ou fermé selon la
		# confirmation de l'utilisateur.
		
		confirmation = input('\nVoulez-vous vraiment quitter (O/N) ?\n> ')
		if confirmation in ['o', 'O']:
			return Menu_Ferme(contenu)
		else:
			return Menu_Ouvert(contenu)
