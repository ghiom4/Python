

def afficher_table(n, operator_str, operator, min=1, max=10):
    if min > max:
        print ("ERREUR")
        return
    for i in range(min, max +1):
        print(f"{i} {operator_str} {n} = {operator(i, n)}")
    print()


afficher_table(2, "*", lambda a, b : a*b)
afficher_table(2, "+", lambda a, b : a+b)