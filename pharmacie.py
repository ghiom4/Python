class Pharmacie:
    def __init__(self, clients=[], medicaments=[]):
        self.clients = clients
        self.medicaments = medicaments

    def nouveau_client(self, nom, credit=0):
        self.clients.append(Client(nom, credit))

    def nouveau_medicament(self, nom, prix):
        self.clients.append(Medicament(nom, prix))

    def menu_principal(self):
        menu = """
1. Clients
2. Médicaments
3. Vente
        """
        print(menu)
        choix = input("Votre choix : ")
        return int(choix)


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.credit = 0

    def paie(self, value):
        self.credit += value

    def nom(self):
        return self.nom
    
    def credit(self):
        return self.credit


class Medicament:
    def __init__(self, nom, prix, stock=0) -> None:
        self.nom = nom
        self.prix = prix
        self.stock = stock
    
    def approvisionne(self, value):
        self.stock += value

    def affichage(self):
        pass


p = Pharmacie()
p.nouveau_client("Robert")
p.menu_principal()
