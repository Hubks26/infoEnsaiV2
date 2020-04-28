from gestion.gestion_des_fichiers.lecteur import Lecteur
from gestion.elements_fichiers.pays import Pays

class Afficheur(Lecteur):
	def numerisation_critere(self, pays, critere):
			if critere == 'superficie':
				txt = pays.get_superficie()
			elif critere == 'population':
				txt = pays.get_pop()
			elif critere == 'croissance démographique':
				txt = pays.get_croissance_demo()
			elif critere == 'inflation':
				txt = pays.get_inflation()   
			elif critere == 'dette':
				txt = pays.get_dette()
			elif critere == 'chômage':
				txt = pays.get_chomage()
			elif critere == 'dépenses santé':
				txt = pays.get_depenses_sante()
			elif critere == 'dépenses éducation':
				txt = pays.get_depenses_education()
			elif critere == 'dépenses militaires':
				txt = pays.get_depenses_militaires()
			else:
				raise KeyError

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
				return "Na"
				
			valeur_numerique = eval(txt)
			
			return valeur_numerique
