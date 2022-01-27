NB_PERSONNES = 2

def est_majeur(age: int):
    if age >=18:
        return True
    return False    


def recuperer_infos_personne(id: int):
    nom = input(f"Nom de la personne {id} : ")
    age = int(input(f"Age de la personne {id} : "))
    return nom, age


def afficher_info_personne(id: int, nom: str, age=0):
    if age == 0:
        print(f"La personne {id} est {nom}.")
    else:
        print(f"La personne {id} est {nom}, son age est {age}.")
    print (f"Le nom comporte {len(nom)} lettres.")
    if est_majeur(age):
        print(f"{nom} est majeur.")
    

def recuperer_et_afficher_infos_personne(id):
    nom, age = recuperer_infos_personne(id)
    afficher_info_personne(id, nom, age)

a = range(1, 5)
print(a[0])
for i in range(1, NB_PERSONNES + 1):
    recuperer_et_afficher_infos_personne(i)
