from affichage.menu_ouvert import Menu_Ouvert
from affichage.gestionnaire_menus import Gestionnaire_des_Menus

class Derouleur:
	# Un dérouleur permet d'afficher les messages de base d'une part
	# et de dérouler les différents menus les uns à la suite des autres d'autre part.

	def __init__(self):
		pass

	def bienvenue(self): # Affiche le message de bienvenue.
		with open('../media/assets/banner.txt', 'r', encoding="utf-8") as asset:
			print(asset.read())

	def aurevoir(self): # Affiche le message de fin.
		with open('../media/assets/a_plus.txt', 'r', encoding="utf-8") as asset:
			print(asset.read())

	def bordure(self): # Affiche une bordure.
		with open('../media/assets/border.txt', 'r', encoding="utf-8") as asset:
			print(asset.read())
			
	def derouler(self): # Méthode permettant de dérouler les menus en commençant avec le menu initial.
		gestionnaire = Gestionnaire_des_Menus()
		menu_actuel = Menu_Ouvert(gestionnaire.contenu_du_menu_initial)
		
		while menu_actuel: 
			# La boucle s'arrète après être tombée sur un menu fermé. En effet, le fait 
			# de "run" un menu fermé renvoie None, ce qui permet de sortir de la boucle.
			
			self.bordure() # On affiche une bordure pour séparer les menus
			
			menu_actuel = menu_actuel.run()
