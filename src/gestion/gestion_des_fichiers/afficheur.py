from gestion.gestion_des_fichiers.lecteur import Lecteur
from gestion.elements_fichiers.pays import Pays

class Afficheur(Lecteur):
	"""Cette classe permet de mettre en forme les données qui seront visible par l'utilisateur"""
	
	def numerisation_critere(self, pays, critere):
		"""Cette méthode rend plus lisible certains nombres.
		Elle permet aussi de supprimer le texte afin d'obtenir uniquement un résultat numérique
		afin de pouvoir s'en servir dans les différentes tâches du data scientist"""
		
			txt = pays.get_critere(critere)

			for i in range(len(txt)):
				if i > 30:
					txt = txt[:i]
					break
				if txt[i] == '+' and txt[i+1] == '+':
					txt = txt[:i-1]
					break
				if txt[i] == ";" or txt[i] == "(":
					txt = txt[:i]
					break
				
			if 'million' in txt:
				txt = txt.replace('million', '*10**6')
			if 'billion' in txt:
				txt = txt.replace('billion', '*10**9')
			if 'trillion' in txt:
				txt = txt.replace('trillion', '*10**12')
				
			lettres_a_supprimer = []
			
			for i in range(len(txt)):
				if i != 0 and txt[i] == '.' and txt[i-1] not in ["0","1","2","3","4","5","6","7","8","9"]:
					lettres_a_supprimer.append(txt[i])
				if txt[i] not in ["0","1","2","3","4","5","6","7","8","9","-",".","*"]:
					lettres_a_supprimer.append(txt[i])
					
			for lettre in lettres_a_supprimer:
				txt = txt.replace(lettre,"")
				
			if len(txt) == 0:
				return "NA"
				
			valeur_numerique = eval(txt)
			
			return valeur_numerique
		
	def simplification(self, txt):
		"""cette méthode permet de simplifier le texte en question afin de ne pas afficher tout le texte
		dans le tableau du résumé d'informations"""
		
		for i in range(len(txt)):
			if i > 20:
					txt = txt[:i] + '...'
					break
			if txt[i] == '+':
				if txt[i+1] == '+':
					txt = txt[:i-1]
					break
			if txt[i] == ";":
				txt = txt[:i]
				break
			if txt[i] == '(':
				txt = txt[:i-1]
				break
		return txt
	
	def liste_triee_selon_critere(self, donnees, critere):
		"""Cette méthode a besoin d'un jeu de donnée et d'un critère. Elle renvoie une liste triée selon
		un critère choisi par le data scientist."""
		
		liste = []
		for num_pays in range(len(donnees)):
			pays = Pays(num_pays, donnees)
			if pays.get_name() and self.numerisation_critere(pays, critere) != 'NA':
				liste.append((self.numerisation_critere(pays, critere), pays))
		liste.sort()
		return liste
