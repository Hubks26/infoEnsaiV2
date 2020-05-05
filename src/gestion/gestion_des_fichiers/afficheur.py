from gestion.gestion_des_fichiers.lecteur import Lecteur
from gestion.elements_fichiers.pays import Pays

class Afficheur(Lecteur):
	def numerisation_critere(self, pays, critere):
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
