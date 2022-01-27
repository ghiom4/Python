import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_VIES = 4
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)

def demander_nombre(min, max):
    nombre_str = input(f"Quel est le nombre magique (entre {min} et {max}) ? ")
    try:
        nombre_int = int(nombre_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        return demander_nombre(min, max)
    else:
        if nombre_int < min or nombre_int > max:
            print(f"ERREUR: Le nombre doit être entre {min} et {max}. Réessayez.")
            return demander_nombre(min, max)
    return nombre_int


for vies in range(NOMBRE_VIES, 0, -1):
    print(f"Il vous reste {vies} vies.")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if NOMBRE_MAGIQUE > nombre:
        print("Le nombre magique est plus grand\n")
    elif NOMBRE_MAGIQUE < nombre:
        print("Le nombre magique est plus petit\n")
    else:
        print("Bravo, vous avez gagné !!!")
        exit()

print("Vous avez perdu !!!")