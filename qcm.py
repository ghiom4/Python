import json
import random
import string

# Le nombre de questions posées au joueur
NB_QUESTIONS = 2

def poser_question(question, num):
    # Affichage de la question
    print(f"Question {num}: {question['titre']}")
    # Affichage des 4 réponses avec la lettre devant
    nb_reponses = len(question['reponses'])
    liste_lettres = string.ascii_lowercase[:nb_reponses]
    for index, lettre in enumerate(liste_lettres):
        print(f"  ({lettre}) {question['reponses'][index][0]}")
    
    # Le joueur saisit la lettre de la réponse
    reponse_joueur = "z"
    while reponse_joueur not in liste_lettres:
        reponse_joueur = input("Votre réponse : ")
        
    id_reponse_joueur = liste_lettres.index(reponse_joueur)

    # On vérifie si le joueur a trouvé la bonne réponse
    if question['reponses'][id_reponse_joueur][1]:
        print("Bonne réponse")
        return True
    else:
        print("Mauvaise réponse")
        return False


# On récupère l'ensemble des questions dans le fichier json
with open("questions.json", "r") as f:
    questionnaire = json.load(f)

score = 0
deja_pose = []


# On pose les NB_QUESTIONS questions
for num in range(1, NB_QUESTIONS + 1):
    # On prend au hasard une question dans la liste
    # Si déjà posée, on en prend un autre
    index = -1
    while index == -1:
        index = random.randint(0, len(questionnaire) - 1)
        if index in deja_pose:
            index = -1
        else:
            deja_pose.append(index)

    # On pose la question et récupère le résultat
    # Si correct, le score est incrémenté
    if poser_question(questionnaire[index], num):
        score += 1
    print()

# A la fin, on affiche le score final du joueur
print(f"Votre score: {score} / {NB_QUESTIONS}")