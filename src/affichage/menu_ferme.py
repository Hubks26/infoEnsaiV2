from affichage.menu import Menu

class Menu_Ferme(Menu): 
	# Le menu fermé hérite de la classe Menu.
	# Son rôle est de terminer le programme.

	def __init__(self, contenu):
		super().__init__(contenu)

	def run(self): # Le fait de 'run' un menu fermé renvoie None -> cela permet d'abréger le déroulement des menus.
		return None
