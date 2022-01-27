import random

class Board:
    def __init__(self) -> None:
        self.grille = [[0]*4 for i in range(4)]
       # self.grille = [[1,2,3,4] for i in range(4)]
    
    def ajouter_2(self):
        y = random.randint(0, 3)
        x = random.randint(0, 3)
        if self.grille[y][x] == 0:
            self.grille[y][x] = 2
        else:
            return self.ajouter_2()

    def inverser(self):
        for y in range(4):
            grille_inversee = self.grille[y][::-1]
            self.grille[y] = grille_inversee

    def renverser(self):
        self.grille = [list(i) for i in list(zip(*self.grille))]

    def afficher(self):
        for i in range(4):
            print(self.grille[i])
        print()
        

gamepanel = Board()
gamepanel.ajouter_2()
gamepanel.ajouter_2()
gamepanel.afficher()
gamepanel.inverser()
gamepanel.afficher()
gamepanel.renverser()
gamepanel.afficher()