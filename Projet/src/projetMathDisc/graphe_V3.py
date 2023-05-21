import time

ID = 0  # identifiant utilisé pour avoir l'unicité des sommets du graphe


class Sommet:
    def __init__(self, val):
        self.val = val
        self.succ = []  # Liste des successeurs du sommet
        self.couleur = "blanc"  # Couleur initiale du sommet (blanc)

    def get_succ(self):
        # Sortie : le nombre de successeurs du sommet
        return self.succ

    def get_couleur(self):
        # Sortie : la couleur du sommet. Blanc pas visité. Gris en cours de visite. Noir déjà visité
        return self.couleur

    def get_valeur_sommet(self):
        # Sortie : la valeur du sommet
        return self.val

    def add_succ(self, val):
        # Entrée : un entier étant le nouveau successeur
        # Sortie : rien
        self.succ.append(val)

    def set_couleur(self, new_couleur):
        # Entrée : une chaîne de caractères étant la nouvelle couleur
        # Sortie : rien
        self.couleur = new_couleur


class Graphe:
    def __init__(self, val):
        # Entrée : un entier
        self.sommets = [Sommet(val)]  # Liste des sommets du graphe

    def get_nb_sommets(self):
        # Sortie : le nombre de sommets dans le graphe
        return len(self.sommets)

    def get_nb_arete(self):
        # Sortie : le nombre d'arêtes (arcs, car orientés, mais ce sont les méthodes utilisées depuis le début)
        return sum(len(s.get_succ()) for s in self.sommets)  # Calcul du nombre d'arêtes de manière efficace

    def get_sommet_num(self, index):
        # Entrée : un entier l'index ième sommet
        # Sortie : le numéro correspondant à l'index ième sommet
        return self.sommets[index].get_valeur_sommet()

    def add_sommet(self, val):
        # Entrée : un entier état la valeur du nouveau sommet
        self.sommets.append(Sommet(val))

    def add_arete(self, v, w):
        # Entrée : deux entiers. Le premier étant le sommet de départ et le deuxième le sommet d'arrivé
        self.sommets[v].add_succ(w)

    def succ(self, index):
        # Entrée : un entier. L'index ième sommet
        # Sortie : les successeurs du sommet
        return self.sommets[index].get_succ()


def DFS(G, v):
    # Entrée : le graphe parcourut, avec le sommet de départ
    G.sommets[v].set_couleur("gris")  # Coloriage du sommet initial en gris
    p = [v]  # Pile pour le parcours en profondeur
    n = []  # Liste des sommets visités dans l'ordre
    while len(p) > 0:
        v = p.pop()
        n.append(v)
        G.sommets[v].set_couleur("noir")  # Coloriage du sommet en noir après son exploration
        for w in G.succ(v):
            if G.sommets[w].get_couleur() == "blanc":
                p.append(w)
                G.sommets[w].set_couleur("gris")  # Coloriage du sommet successeur en gris pour exploration ultérieure
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
for i in range(1000000):
    DFS(graphe, 0)
end_time = time.time()

# Affichage du temps d'exécution
execution_time = (end_time - start_time) / 1000000
print("Temps d'exécution : %.10f secondes" % execution_time)
"""

"""
l'algorithme DFS est plus optimal car il va utiliser une liste d'adjacence se qui est le plus optimal pour cette algorithme.
(voir cours) et de plus, pour le coloriage des sommets, on peut utiliser un dictionnaire avec les sommets comme clefs et 
la couleur comme valeur. Se qui réduit drastiquement le temps de recherche pour la condition de la ligne 
"if visite.get(w) not in ["noir", "gris"]:" car le temps de recherche dans un dictionnaire se fait en O(1) car présence d'une clef.
Contrairement au temps de recherche dans une liste qui se fait en O(n) avec n la taille de la liste.
"""
