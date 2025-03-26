# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:23:43 2024

@author: MS
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def creation_matrice():
    """
    Création d'un matrice (remplacer celle ci-dessous)
    np.inf represente l'abscence de lien entre deux noeuds
    Si il y a une valeurs alors elle correspond au poids entre les deux noeuds'
    """
    Chemins = np.array([[np.inf, 93, np.inf, np.inf, 86, np.inf],
                        [93, np.inf, 56, 47, np.inf, np.inf],
                        [np.inf, 56, np.inf, np.inf, np.inf, 62],
                        [np.inf, 47, np.inf, np.inf, 34, np.inf],
                        [86, np.inf, np.inf, 34, np.inf, 134],
                        [np.inf, np.inf, 62, np.inf, 134, np.inf]])
    return Chemins

# Exemple d'utilisation
Matrice = creation_matrice()

# Création du graphe à partir de la matrice
G = nx.from_numpy_matrix(Matrice, create_using=nx.DiGraph)

# Positionnement des noeuds pour l'affichage
pos = nx.spring_layout(G)

# Affichage des noeuds
nx.draw_networkx_nodes(G, pos, node_size=700)

# Affichage des arêtes avec les poids
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Affichage des poids sur les arêtes
nx.draw_networkx_labels(G, pos)

# Affichage du graphe
plt.title("Graphe pondéré")
plt.axis('off')
plt.show()