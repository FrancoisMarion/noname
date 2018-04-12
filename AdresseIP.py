# Programme qui doit demander en input les adresses IP et générer un tableau par la suite
# Une fois les adresses rentrées, on peut modifier le tableau généré par les adresses.

# import os
# import subprocess

var = []
tableau = []

booleen = True
# Fonction qui va demander les adresses puis les enmagasiner dans la variable tableau
def ftest():
	global var, tableau
	# Créer fonction pour while
	i = 1
	while True:

		var.append(input("Quelle est l'adresse IP?\n"))
		demande = input("Est-ce la dernière adresse? o/n\n")
		if demande.lower() in ['o']:
			print("\n") # sépare réponses du résultat final affiché
			break
		elif demande.lower() in ['n']:
			i = i+1
		else:
			print("Il faut répondre par o ou n pour Oui ou Non")
	# Juste voir ce qu'il doit y avoir au total dans le tableau final, et reste
	# à insérer valeurs de var dans tableau dans les colonnes appropriées
	for j in range(i):
		print(var[j]) # restera à concaténer une phrase dans cette variable
		tableau = str1[j] + var[j] + str2[j]
		# print (str1 + var[j] + str2)

		
def switch(choix):
	return {'1':}.get

# Option 1
def afficher():
	global var, tableau
	print(tableau)

# Maintenant, fonction modification si erreur
def correction():
	# option 2
	global var, tableau
	# Choisir l'adresse IP à modifier
	IP_changer = int(input())
	if IP_changer < 1 or IP_changer > len(var):
		return print("Cette élément n'existe pas\n")
	else:
		var[IP_changer] = input()
		print("La nouvelle adresse est maintenant %s\n", var[IP_changer])

# Option 3		
def fermer():
	booleen = False


# Option 4
def ajout():
global var, tableau
	var.append(input("Adresse à ajouter\n")
	tableau.append(var(len(var)))
	print(tableau\n)
	
	
# Option 5
def effacer():
	global var, tableau
	print(tableau)
	IP_effacer = int(input(

	
	
# Menu interactif switch case dans un while true

def main():
	global var, tableau
	print("Choisissez parmi les options suivantes: \n")
	print("1: Afficher la liste des adresses IP\n")
	print("2: Modifier une adresse IP\n")
	print("3: Fermer le programme\n")
	print("4: Ajouter une adresse\n")
	print("5: Effacer une adresse\n")
	
	valeur = [1,2,3,4,5]
	option = int(input())
	if option == 1:
		afficher()
	elif option == 2:
		correction()
	elif option == 3:
		fermer()
	elif option == 4:
		ajout()
	elif option == 5:
		effacer()
	else:
	print(" Veuillez entrer un nombre entre 1 et 5 \n")
	
# Essayer avec le switch équivalent, soit les dictionnaires


	
ftest()


while booleen:

	main()
