
class Menu:
	# Menu est une classe abstraite qui permet de définir les menus.
	# Un menu est défini à l'aide d'un dictionnaire :
	# contenu -> {"question" : string, "options" : list_of_strigs, "actions" : list_of_functons,
	# "individu" : Individu(), "chemin de la recherche", list_of_strigs}
	# La méthode run est propre à tous les menus.

	def __init__(self, contenu):
		self.contenu = contenu

	def run(self):
		raise NotImplemented()
