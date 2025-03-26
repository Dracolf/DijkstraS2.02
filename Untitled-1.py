import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def creation_matrice():
    """
    Création d'un matrice (remplacer celle ci-dessous)
    np.inf represente l'absence de lien entre deux noeuds
    Si il y a une valeur alors elle correspond au poids entre les deux noeuds
    """
    Chemins = np.array([[np.inf, 93, np.inf, np.inf, 86, np.inf],
                        [93, np.inf, 56, 47, np.inf, np.inf],
                        [np.inf, 56, np.inf, np.inf, np.inf, 62],
                        [np.inf, 47, np.inf, np.inf, 34, np.inf],
                        [86, np.inf, np.inf, 34, np.inf, 134],
                        [np.inf, np.inf, 62, np.inf, 134, np.inf]])
    return Chemins

def afficher_graphe(matrice):
    G = nx.from_numpy_matrix(matrice)
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Test de la fonction
matrice = creation_matrice()
afficher_graphe(matrice)