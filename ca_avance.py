import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

g = nx.Graph()
g.add_nodes_from(range(5))
g.add_edges_from([(0,1),(3,4),(4,2),(1,3),(4,0),(1,2),(1,5)])

options = {
    'node_color' : 'pink',
    'node_size'  : 550,
    'edge_color' : 'tab:grey',
    'with_labels': True
}

adjacencePoids = np.array([[np.inf, 93, np.inf, np.inf, 86, np.inf],
                            [93, np.inf, 56, 47, np.inf, np.inf],
                            [np.inf, 56, np.inf, np.inf, np.inf, 62],
                            [np.inf, 47, np.inf, np.inf, 34, np.inf],
                            [86, np.inf, np.inf, 34, np.inf, 134],
                            [np.inf, np.inf, 62, np.inf, 134, np.inf]])

nomNoeuds = ['T','C','N','M','F','P']

def choixLettre(i,j):
    a = nomNoeuds[i]
    b = nomNoeuds[j]
    return a,b    

def is_oriented(matrix):
    transpose = np.transpose(matrix)
    return not np.array_equal(matrix, transpose)

if not is_oriented(adjacencePoids):
    G = nx.DiGraph()
    nombre_lignes, nombre_colonnes = adjacencePoids.shape
    
    for i in range(nombre_colonnes):
        for j in range(nombre_lignes):
            if adjacencePoids[i][j] != np.inf:
                a,b = choixLettre(i, j)
                G.add_edge(a, b, weight=adjacencePoids[i][j])
    
    val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 1.0}
    
    values = [val_map.get(node, 0.45) for node in G.nodes()]
    edge_labels = dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    red_edges = [('C','D'),('D','A')]
    edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    
    pos = nx.circular_layout(G)
    pos_higher = {}
    offset_x = 0.05
    offset_y = 0.1
    for k, v in pos.items():
        pos_higher[k] = (v[0] + offset_x, v[1] + offset_y)
    
    nx.draw_networkx_edge_labels(G, pos_higher, edge_labels=edge_labels, font_color='blue')
    nx.draw(G, pos, node_color='pink', with_labels=True, node_size=1000, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
    pylab.show()
else:
    print("nope")