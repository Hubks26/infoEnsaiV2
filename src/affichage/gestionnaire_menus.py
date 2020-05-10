from affichage.menu_ouvert import Menu_Ouvert
from acteurs.individu import Individu
from acteurs.consultant import Consultant
from acteurs.geographe import Geographe
from acteurs.data_scientist import Data_Scientist
from acteurs.admin import Admin

class Gestionnaire_des_Menus:
	# Un gestionnaire des menus permet de définir le menu initial et 
	# les menus de choix des options de chaque acteur.
	
	def __init__(self):
		# On définit en attribu du gestionnaire des menus 
		# le contenu du menu initial de l'application
		# ainsi que le contenu du menu regroupant toutes
		# les actions disponibles.
		
		self.contenu_du_menu_initial = {
			
			'question' : 
				'Quel est votre statut ?',
			'options' : 
			[
				'Consultant', 
				'Data Scientist', 
				'Géographe',
				'Administrateur'
			],
			'options basiques' :
			[
				['QUITTER', 'Q']
			],
			'actions' : 
			[
				(lambda contenu : self.taches_permises([1], Consultant())),
				(lambda contenu : self.taches_permises([0, 1, 2, 3], Data_Scientist())),
				(lambda contenu : self.taches_permises([0, 1, 4], Geographe())),
				(lambda contenu : self.taches_permises([0, 1, 2, 3, 4, 5], Admin())),
				Individu().quitter
			],
			'individu' :
				Individu(),
			'pseudo' :
				None
		}
			
		self.contenu_du_menu_des_acteurs = {
	
			'question' : 
				'Que voulez vous faire ?',
			'options' : 
			[   
				'Se connecter',
				"Afficher les données d'un pays",
				'Acceder aux résumés statistiques',
				'Représentations graphiques',
				'Décider de valider ou de refuser une correction',
				'Créer ou supprimer un compte',
			],
			'options basiques' :
			[
				['RETOUR AU MENU DE CHOIX DU STATUT', 'R'],
				['QUITTER', 'Q']
			],
			'actions' : 
			[
				lambda contenu : contenu['individu'].se_connecter(contenu),
				lambda contenu : contenu['individu'].afficher_pays(contenu),
				(lambda contenu : contenu['individu'].resume_stat(contenu)),
				(lambda contenu : contenu['individu'].representation_graphique(contenu)),
				(lambda contenu : contenu['individu'].gestion_corrections(contenu)),
				(lambda contenu : contenu['individu'].gestion_compte(contenu)),
				(lambda contenu : Menu_Ouvert(self.contenu_du_menu_initial)),
				Individu().quitter
			],
			'individu' :
				Individu(),
			'pseudo' :
				None
		}
	
	def taches_permises(self, liste_des_taches_permises, individu):
		# Cette fonction permet de diriger l'utilisateur vers le menu où sont
		# poposé toutes les actions qu'il a le droit d'effectuer.
		# Elle prend en argument un liste des numéros de tâches permises pour
		# l'utilisateur et le statut de l'utilisateur. individu est donc de 
		# type Individu(), il peut s'agir d'un Consultant, d'un Géographe,
		# d'un data_scientist ou d'un administrateur.
		# Cette fonction renvoie le menu corresondant à l'utilisateur.
		
		contenu_menu_acteur = {}
		contenu_menu_acteur['individu'] = individu
		contenu_menu_acteur['question'] = self.contenu_du_menu_des_acteurs['question']
		contenu_menu_acteur['options'] = [self.contenu_du_menu_des_acteurs['options'][i] for i in liste_des_taches_permises]
		contenu_menu_acteur['options basiques'] = self.contenu_du_menu_des_acteurs['options basiques']
		
		contenu_menu_acteur['actions'] = []
		for i in range(len(self.contenu_du_menu_des_acteurs['actions'])):
			if i in liste_des_taches_permises or i >= len(self.contenu_du_menu_des_acteurs['options']):
				contenu_menu_acteur['actions'].append(self.contenu_du_menu_des_acteurs['actions'][i])
				
		return Menu_Ouvert(contenu_menu_acteur)
