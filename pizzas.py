def afficher(collection, nb=-1):
    #collection.sort()
    if nb == -1:
        c = collection
    else:
        c = collection[:nb] 
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return
    print(f"---- LISTE DES PIZZAS ({len(c)}) ----")
    for element in c:
        print(element)
    print()
    print("Première pizza :", c[0])
    print("Dernière pizza :", c[-1])


def ajouter_pizza_utilisateur(collection):
    pizza = input("Pizza à ajouter : ")
    if pizza.lower() in collection:
        print("ERREUR - La pizza existe déjà")
    else:
        collection.append(pizza.lower())
        


pizzas = ["4 fromages", "végétarienne", "calzone", "napolitaine"]

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 2)
afficher(pizzas)