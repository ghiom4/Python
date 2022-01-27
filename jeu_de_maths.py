import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question(min, max):
    # Choix aléatoire de 2 nombres
    nombre1 = random.randint(min, max)
    nombre2 = random.randint(min, max)

    # Choix aléatoire du type de calcul
    type = random.randint(0, 1)
    if type == 0:
        calcul = nombre1 + nombre2
        operateur = "+"
    else:
        calcul = nombre1 * nombre2
        operateur = "x"

    nombre = 0
    
    while nombre == 0:
        nombre_str = input(f"Calculez: {nombre1} {operateur} {nombre2} = ")

        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int == calcul:
                return True
            return False


score = 0

# On pose les questions
for i in range(0, NB_QUESTIONS ):
    print(f"Question n°{i + 1} sur {NB_QUESTIONS}")
    if poser_question(NOMBRE_MIN, NOMBRE_MAX):
        score += 1
        print("Réponse correcte")
    else:
        print("Réponse incorrecte")
    print()

# Affichage du score
print(f"Votre score: {score} / {NB_QUESTIONS}")

# Affichage de l'évaluation en fonction du score
moyenne = int(NB_QUESTIONS / 2)
if score == NB_QUESTIONS:
    print("Excellent!")
elif score == 0:
    print("Révisez vos maths!")
elif score >= moyenne:
    print("Pas mal!")
else:
    print("Peut mieux faire !")