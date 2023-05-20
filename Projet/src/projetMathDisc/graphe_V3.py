import time

ID = 0  # identifiant utilisé pour avoir l'unicité des sommets du graphe


class Node:  # la classe permet de représenter un node de la liste chaînée
    def __init__(self, data):
        # Entrée : un entier avec la valeur du node
        # Sortie : rien
        self.data = data
        self.next = None


class LinkedList:  # la classe représente une liste chaînée et permet de représenter
                   # les liens de filiations entre les sommets du graphe

    def __init__(self, data):
        # Entrée : un entier avec la valeur du node
        self.tete = Node(data)
        self.nb_successeurs = 0  # nombre de successeurs

    def add_node(self, val):
        # Entrée : nouveau node ajouté à la liste
        # Sortie : rien
        new_node = Node(val)
        if self.tete is None:
            self.tete = new_node
        else:
            current = self.tete
            while current.next:
                current = current.next
            current.next = new_node

    def add_succ(self, val):
        # Entrée : un entier représentant le nouveau successeur
        if self.tete is not None:
            current = self.tete
            while current.next:
                current = current.next
            current.next = Node(val)
            self.nb_successeurs += 1

    def get_nb_succ(self):
        return self.nb_successeurs

    def get_valeur_sommet(self):
        if self.tete is not None:
            return self.tete.data
        return None

    def get_succ(self):
        successors = []
        current = self.tete.next
        while current:
            successors.append(current.data)
            current = current.next
        return successors


class Graphe:
    def __init__(self, val):
        # Entrée : un entier
        # Sortie : rien
        # Crée un graphe avec un sommet de valeur val définit par une matrice 1x1
        self.sommets = []
        self.sommets.append(LinkedList(val))

    def get_nb_sommets(self):
        # Sortie : le nombre de sommets dans le graphe
        return len(self.sommets)

    def get_nb_arete(self):
        nb_aretes = 0
        for sommet in self.sommets:  # parcours de tous les sommets
            nb_aretes += sommet.get_nb_succ()
        return nb_aretes

    def get_sommet_num(self, index):
        # Entrée : l'id d'un sommet
        # Sortie : la valeur de ce sommet, un entier
        return self.sommets[index].get_valeur_sommet()

    def add_sommet(self, val):
        # Entrée : un entier, une valeur
        # Sortie : rien
        self.sommets.append(LinkedList(val))

    def add_arete(self, v, w):
        # Entrées : deux entiers, les Id des sommets
        # Sortie : rien
        # Ajoute l'arête orienté. Les poids sur les arêtes ne sont pas gérés.
        self.sommets[v].add_succ(w)

    def succ(self, index):
        # Entrée : l'id d'un sommet, un entier
        # Sortie : la liste chaînée des numéros des sommets, un tableau d'entiers
        return self.sommets[index].get_succ()


def DFS(G, v):
    visite = {v: "gris"}  # utilisation d'un dictionnaire pour le coloriage des sommets
    p = [v]
    n = []
    while len(p) > 0:
        v = p.pop()
        visite[v] = "noir"
        n.append(v)
        # print(v)
        for w in G.succ(v):
            if visite.get(w) not in ["noir", "gris"]:
                p.append(w)
                visite[w] = "gris"
            w = G.succ(w)
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
# arête = id
G.add_arete(0, 1)
G.add_arete(1, 2)
G.add_arete(2, 3)
G.add_arete(2, 4)

print("Nb sommets : ", G.get_nb_sommets())
print("Nb arêtes : ", G.get_nb_arete())
print("Valeur sommet num 1 : ", G.get_sommet_num(1))

print("succ de 2 : ")
for w in G.succ(2):
    print(w)

n = DFS(G, 0)

print(n)

ID = 0

# ajout des sommets
G1 = Graphe(1)
for i in range(2, 7):
    G1.add_sommet(i)

# ajout des arêtes
for i in range(1, 4):
    G1.add_arete(0, i)

G1.add_arete(3, 2)
G1.add_arete(2, 5)
G1.add_arete(2, 4)
G1.add_arete(4, 2)
G1.add_arete(5, 2)
G1.add_arete(5, 4)

# ajout des boucles
for i in [0, 1, 3, 4, 5]:
    G1.add_arete(i, i)

print("Nb sommets : ", G1.get_nb_sommets())
print("Nb arêtes : ", G1.get_nb_arete())
print("Valeur sommet num 1 : ", G1.get_sommet_num(1))

print("succ de 2 : ")
for w in G1.succ(2):
    print(w)

n = DFS(G1, 0)

print(n)

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

"""
l'algorithme DFS est plus optimal car il va utiliser une liste d'adjacence se qui est le plus optimal pour cette algorithme.
(voir cours) et de plus, pour le coloriage des sommets, on peut utiliser un dictionnaire avec les sommets comme clefs et 
la couleur comme valeur. Se qui réduit drastiquement le temps de recherche pour la condition de la ligne 
"if visite.get(w) not in ["noir", "gris"]:" car le temps de recherche dans un dictionnaire se fait en O(1) car présence d'une clef.
Contrairement au temps de recherche dans une liste qui se fait en O(n) avec n la taille de la liste.


Temps d'exécution : 0.0000019952 secondes
"""
