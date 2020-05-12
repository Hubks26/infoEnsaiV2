# Projet_ENSAI

Le Projet "Traitement de données" s’adresse aux étudiants en 1 ère année à l’Ensai.
"Vous devez mettre en avant le côté Programmation Orientée Objet du langage Python. L’architecture de vos codes doit être bien structurée, bien documentée."

___

## Traitement de données
[Python] Une application permettant la gestion d'une banque de données fournie par la CIA.

___

## Comment lancer l'application

Ce programme fonctionne avec python 3.6.9 et nécessite les bibliothèques matplotlib, pandas, numpy et scikit-learn.

Pour installer matplotlib, panda et numpy sur linux vous pouvez utiliser les commandes suivantes dans :

sudo apt-get install python3-pip

pip3 install matplotlib pandas numpy

Pour installer scikit-learn sur linux vous pouvez utiliser les commandes suivantes dans :

sudo apt-get install python3-pip

pip3 install -U scikit-learn

Pour lancer l'application, executez le fichier main.py depuis le répertoire src : python3 main.py

Pour que vous puissiez accéder à toutes les fonctionnalités nous vous mettons à disposition le compte administrateur suivant :

pseudo : invite

password : 0123

___

## Comment lancer les tests ?

Sous Linux, pour lancer le test fonctionnel, il suffit d'utiliser la commande suivante (depuis le répertoire src):

cat tests/test_fonctionnel/commandes.txt | python3 main.py

Sous Linux, pour lancer les tests unitaires, il suffit d'utiliser les commandes suivantes (depuis le répertoire src):

python3 -m unittest tests/tests_unitaires/test_afficheur.py

python3 -m unittest tests/tests_unitaires/test_section.py
___

## Auteurs

-Dugor Pierre
-Goussian Alex
-Lacaille Adrien

