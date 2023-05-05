class Graphe:
    def __init__(self, val):
        # Entrée : un entier
        # Sortie : rien
        # Crée un graphe avec un sommet de valeur val définit par une matrice 1x1
        self.matrice = Matrice(1)
        self.matrice[0][0] = val
        self.nb_sommets = 1

    def get_nb_sommets(self):
        return self.nb_sommets

    def get_nb_arete(self):
        nb_aretes = 0
        for i in range(self.nb_sommets):
            for j in range(self.nb_sommets):
                if i != j:
                    nb_aretes += self.matrice[i][j]
        return nb_aretes

    def get_sommet_num(self, i):
        # Entrée : l'id d'un sommet
        # Sortie : la valeur de ce sommet, un entier
        return self.matrice[i][i]

    def add_sommet(self, val):
        # Entrée : un entier, une valeur
        # Sortie : rien
        self.nb_sommets += 1
        new_matrice = Matrice(self.nb_sommets)
        for i in range(self.nb_sommets-1):
            for j in range(self.nb_sommets-1):
                new_matrice[i][j] = self.matrice[i][j]
        new_matrice[self.nb_sommets-1][self.nb_sommets-1] = val
        self.matrice = new_matrice
        # Incide : créer une matrice de taille n+1xn+1, tout recopier puis ajouter le sommet.

    def add_arete(self, v, w):
        # Entrées : deux entiers, les Id des sommets
        # Sortie : rien
        # Ajoute l'arête orienté. Les poids sur les arêtes ne sont pas gérés.
        self.matrice[v][w] = 1

    def succ(self, i):
        # Entrée : l'id d'un sommet, un entier
        # Sortie : la liste des numéros des sommets, un tableau d'entiers
        succ = []
        for j in range(self.nb_sommets):
            if j != i and self.matrice[i][j] == 1:
                succ.append(j)
        return succ


def DFS(G, v):
    # rien ne doit changer par rapport à la v1
    p = [v]
    n = []
    while len(p) > 0:
        v = p.pop()
        print(v)
        for w in G.succ(v):
            if not (w in p) and not (w in n):
                p.append(w)
        n.append(v)
    n
    return n
