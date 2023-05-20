# -------------GRAPHES ORIENTES----------------#
# Avec matrices d'adjacences : la diagonale contient les valeurs des sommets
import time


def Matrice(n):
    # Entrée : un entier
    # Sortie : une matrice de taille nxn avec des 0 partout
    return [[0] * n for i in range(0, n)]


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
        for i in range(self.nb_sommets - 1):
            for j in range(self.nb_sommets - 1):
                new_matrice[i][j] = self.matrice[i][j]
        new_matrice[self.nb_sommets - 1][self.nb_sommets - 1] = val
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
        # print(v)
        for w in G.succ(v):
            if not (w in p) and not (w in n):
                p.append(w)
        n.append(v)
    n
    return n


# ici non plus rien ne doit changer par rapport à la v1
# création du graphe :
#       5
#       |
#       8
#       |
#       5
#     /  \
#    2   6
G = Graphe(5)
G.add_sommet(8)
G.add_sommet(5)
G.add_sommet(2)
G.add_sommet(6)
print("mat : ", G.matrice)
# arête = id
G.add_arete(0, 1)
G.add_arete(1, 2)
G.add_arete(2, 3)
G.add_arete(2, 4)

print("mat : ", G.matrice)
print("Nb sommets : ", G.get_nb_sommets())
print("Nb arêtes : ", G.get_nb_arete())
print("Valeur sommet num 1 : ", G.get_sommet_num(1))

print("succ de 2 : ")
for w in G.succ(2):
    print(w)

print("===DFS====")
n = DFS(G, 0)
print("liste postfixe inversée : ", n)

"""
# Création du graphe avec 1000 sommets
graphe = Graphe(0)
for i in range(1, 1000):
    graphe.add_sommet(i)
graphe.add_arete(0, 1)
graphe.add_arete(0, 2)
graphe.add_arete(1, 2)

# Exécution de l'algorithme DFS avec chronomètre
start_time = time.time()
for i in range(10000):
    DFS(graphe, 0)
end_time = time.time()

# Affichage du temps d'exécution
execution_time = (end_time - start_time) / 10000
print("Temps d'exécution : %.10f secondes" % execution_time)
Temps d'exécution : 0.0001504596 secondes
"""

"""
l'implémentation n'est pas optimale pour l'ajout de sommet. Car il va recréer une nouvelle matrice et parcourir l'ancien
pour initialiser la nouvelle matrice.
la recherche du nombre d'arêtes n'est pas optimal non plus optimal. Car il va parcourir toute la matrice.
Pour l'algorithme DFS tous les sommets sont parcourus  ainsi que toute les arêtes. De plus pour la recherche de successeurs 
cela se fait en 0(N) avec N le nombre de sommets car on utilise une liste pour faire cela.
"""
