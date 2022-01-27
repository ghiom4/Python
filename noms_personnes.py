liste_noms = []

while True:
    nom = input("Nom de la personne : ")
    if nom == "":
        break
    liste_noms.append(nom)

for i in liste_noms:
    print(f"Le nom est : {i}")