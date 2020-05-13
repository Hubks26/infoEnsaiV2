from affichage.menu import Menu

class Menu_Ouvert(Menu): 
	# Le menu ouvert hérite de la classe Menu.

	def __init__(self, contenu):
		super().__init__(contenu)

	def run(self): # La méthode run permet d'afficher le menu et d'interagir avec l'utilisateur.
		options = self.contenu['options']
		options_basiques = self.contenu['options basiques']
		nb_options = len(options)
		actions = self.contenu['actions']
		
		print('{}\n'.format(self.contenu['question'])) # On affiche la question du menu.
		
		for i, opt in enumerate(options): # On affiche les options du menu.
			print('[{}] {}'.format(i+1, opt)) 
			
		if len(options_basiques) > 0 : print('')
		
		for opt_base in options_basiques: # On affiche les options de base : QUITTER, RETOUR...
			print('[{}] {}'.format(opt_base[1], opt_base[0]))
		 
		codes_options_base = [opt_base[1] for opt_base in options_basiques] # Liste des codes des options basiques ! Q, R...
			
		while True: # On demande à l'utilisateur de choisir une option.
			choix = input('\n> ')
			try:
				choix = int(choix)
			except ValueError:
				if choix.upper() not in codes_options_base:
					print('\nVotre réponse ne correspond à aucune option.')
				else :
					choix = choix.upper()
					break
				continue
			if choix <= 0 or choix > nb_options:
				print('\nVotre réponse ne correspond à aucune option.')
				continue
			break
		
		if choix in codes_options_base:
			indice = codes_options_base.index(choix)
			return actions[nb_options + indice](self.contenu) # On applique la fonction qui correspond au choix de l'utilisateur.
		else:
			return actions[choix-1](self.contenu) # On applique la fonction qui correspond au choix de l'utilisateur.
