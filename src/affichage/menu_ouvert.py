from affichage.menu import Menu

class Menu_Ouvert(Menu): 
	# Le menu fermé hérite de la classe Menu.

	def __init__(self, contenu):
		super().__init__(contenu)

	def run(self): # La méthode run permet d'afficher le menu et d'intéragir avec l'utilisateur.
		options = self.contenu["options"]
		nb_options = len(options)
		actions = self.contenu["actions"]
		
		print("{}\n".format(self.contenu["question"])) # On affiche la question du menu.
		
		for i, opt in enumerate(options): # On affiche les options du menu.
			print("[{}] {}".format(i+1, opt)) 
			
		while True: # On demande à l'utilisateur de choisir une option.
			choix = input("\n> ")
			try:
				choix = int(choix)
			except ValueError:
				print("\nLa réponse attendue doit être un entier.")
				continue
			if choix <= 0 or choix > nb_options:
				print("\nLa réponse attendue doit être comprise entre 1 et {}.".format(nb_options))
				continue
			break
		return actions[choix-1](self.contenu) # On applique la fonction qui correspond au choix de l'utilisateur.
