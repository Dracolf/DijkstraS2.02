#Importation de toutes les bibliothèques
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

inf = float('inf')
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def creation_matrice():
    #Permet d'utiliser les varaible dans tous le programme
    global adjacencePoids
    global nomNoeuds
    
    """
    #Modifier les valeurs entre parenthèse pour modifer la matrice
    adjacencePoids = np.array([[inf,7,inf,-4],
                               [inf,inf,inf,3],
                               [2, inf,inf,inf],
                               [inf,inf,1,inf]])
    adjacencePoids = adjacencePoids.astype('float64')
    
    #Modifier les lettre pour modifier les noms des noeuds du graph
    nomNoeuds = ['A', 'B', 'C', 'D']"""
    
    
    
    #Modifier les valeurs entre parenthèse pour modifer la matrice
    adjacencePoids = np.array([[inf,6,3,inf,inf],
                               [inf, inf, inf, 5, 1],
                               [inf, 2, inf, inf, inf],
                               [inf, 1, inf, inf, -5],
                               [inf, inf, 2, inf, inf]])
    adjacencePoids = adjacencePoids.astype('float64')
    
    #Modifier les lettre pour modifier les noms des noeuds du graph
    nomNoeuds = ['A', 'B', 'C', 'D', 'E']
    
    
    """
    #Modifier les valeurs entre parenthèse pour modifer la matrice
    adjacencePoids = np.array([[inf, 93, inf, inf, 86, inf],
                                [93, inf, 56, 47, inf, inf],
                                [inf, 56, inf, inf, inf, 62],
                                [inf, 47, inf, inf, 34, inf],
                                [86, inf, inf, 34, inf, 134],
                                [inf, inf, 62, inf, 134, inf]])
    adjacencePoids = adjacencePoids.astype('float64')
    
    #Modifier les lettre pour modifier les noms des noeuds du graph
    nomNoeuds = ['T','C','N','M','F','P']"""

"""
DEMANDER SI ON PEUT DANS CETTE FONCTION APPELER L'AUTRE GRAPHE2 ET JUSTE METTRE 50% DE FLECHES
"""
def graphe(n, a, b):
    graphe2(n, 0.5, a, b)
    
    
    """global adjacencePoids
    global nomNoeuds
    
    # Nombre total d'éléments dans la matrice
    total_elements = n * n
    
    # Initialisation de la matrice adjacencePoids avec des infinis
    adjacencePoids = np.full((n, n), np.inf)
    
    # Remplacement d'une partie des éléments par des valeurs aléatoires dans l'intervalle [a, b[
    num_integer = total_elements // 2
    
    #Les nombres aléatoires
    random_integers = []
    for i in range(num_integer):
        random_integers.append(np.random.randint(a, b))
    
    #Les indices aléatoires (en nombbre compris entre 0 et total_elements)
    indices = []
    for i in range(num_integer):
        valeur_aleatoire = np.random.randint(0, total_elements)
        while valeur_aleatoire in indices:
            valeur_aleatoire = np.random.randint(0, total_elements)
        indices.append(valeur_aleatoire)
    
    #Conversion des indices en coordonnées de la matrice
    lig_indices = []
    col_indices = []
    for el in indices:
        lig_indices.append(el // n)
        col_indices.append(el % n)
    
    # Remplacement des éléments infinis par des valeurs entières
    for i in range(num_integer):
        adjacencePoids[lig_indices[i]][col_indices[i]] = random_integers[i]
    
    nomNoeuds = []
    for i in range(n):
        nomNoeuds.append(alphabet[i])"""
        
def graphe2(n, p, a, b):
    global adjacencePoids
    global nomNoeuds
    
    # Nombre total d'éléments dans la matrice
    total_elements = n * n
    
    # Initialisation de la matrice adjacencePoids avec des infinis
    adjacencePoids = np.full((n, n), np.inf)
    
    # Remplacement d'une partie des éléments par des valeurs aléatoires dans l'intervalle [a, b[
    num_integer = round(total_elements * p)
    
    #Les nombres aléatoires
    random_integers = []
    for i in range(num_integer):
        random_integers.append(np.random.randint(a, b))
    
    #Les indices aléatoires (en nombbre compris entre 0 et total_elements)
    indices = []
    for i in range(num_integer):
        valeur_aleatoire = np.random.randint(0, total_elements)
        while valeur_aleatoire in indices:
            valeur_aleatoire = np.random.randint(0, total_elements)
        indices.append(valeur_aleatoire)
    
    #Conversion des indices en coordonnées de la matrice
    lig_indices = []
    col_indices = []
    for el in indices:
        lig_indices.append(el // n)
        col_indices.append(el % n)
    
    # Remplacement des éléments infinis par des valeurs entières
    for i in range(num_integer):
        adjacencePoids[lig_indices[i]][col_indices[i]] = random_integers[i]
    
    nomNoeuds = []
    for i in range(n):
        nomNoeuds.append(alphabet[i])
        

#Permet de choisir les nom des Noeuds parmis la liste
def choix_nom_noeuds(i,j):
    a = nomNoeuds[i]
    b = nomNoeuds[j]
    return a,b

#Renvoi vrai ou faux en fonction de si le graph est orienté ou non
def est_oriente(matrix):
    transpose = np.transpose(matrix)
    return not np.array_equal(matrix, transpose)

def chemin_en_rouge(listeSommets):
    leChemin = []
    
    for i in range(len(listeSommets)-1):
        leChemin.append((listeSommets[i], listeSommets[i+1]))
    
    return leChemin


#Dijkstra
def dijkstra(M, d):
    global red_edges
    
    iteration = 1
    
    #Le nombre de noeuds
    n = len(nomNoeuds)
    
    #Récupération des flèches    
    Fleche = []
    for i in range(n):
        for j in range(n):
            if M[i][j] != inf:
                Fleche.append([i,j])
    
    #initialisation
    Sommet = []
    for i in range(n):
        if i == d:
            Sommet.append([i, 0, d, True])
        elif [d,i] in Fleche:
            Sommet.append([i, M[d][i], d, False])
        else:
            Sommet.append([i, inf, None, False])

    A = []
    A.append(Sommet[d])
    
    while len(A) < n and iteration <= n-1:
        
        sommet_dispo = []
        for el in Sommet:
            if not el[3] and el[1] != inf:
                sommet_dispo.append(el)
        
        if len(sommet_dispo) >= 1:
            plus_faible = sommet_dispo[0]
            for sd in sommet_dispo:
                if sd[1] < plus_faible[1]:
                    plus_faible = sd
            
            Sommet[plus_faible[0]][3] = True
            A.append(plus_faible)
            
            for el in Sommet:
                if not el[3]:
                    if [plus_faible[0], el[0]] in Fleche:
                        if M[plus_faible[0]][el[0]] + plus_faible[1] < el[1]:
                            el[1] = M[plus_faible[0]][el[0]] + plus_faible[1]
                            el[2] = plus_faible[0]
        
        iteration += 1
    
    
    for element in Sommet:
        if element[0] != d:
            if element[1] == inf or element[2] == None:
                print(nomNoeuds[element[0]], ": sommet non joignable depuis ", nomNoeuds[d],
                      "par un chemin dans le graphe G.")
            else:
                #Création d'une liste qui va contenir le chemin du départ vers la destination
                Liste = []
                Liste.append(nomNoeuds[element[0]])
                sommet_suivant = Sommet[element[0]][2]
                
                #Si le dernier sommet ajouté a la liste et le sommet de départ alors on a finit de retracer le chemin 
                while Liste[-1] != nomNoeuds[d]:
                    #On ajoute les noms des sommets et non leur indices dans la liste des noms
                    Liste.append(nomNoeuds[sommet_suivant])
                    #Permet de recalculer le sommet suivant
                    sommet_suivant = Sommet[sommet_suivant][2]
                    
                #Affichage avec tout les éléments
                print(nomNoeuds[element[0]]," : chemin ", Liste[::-1], " et de poids ", element[1])
        

#Bellman-Ford
def Bellman_Ford(M, d):
    global red_edges
    
    #initialisation à True pour rentrer dans la boucle
    changement = True
    iteration = 1
    
    #Le nombre de noeuds
    n = len(nomNoeuds)
    
    
    #Récupération des flèches    
    Fleche = []
    for i in range(n):
        for j in range(n):
            if M[i][j] != inf:
                Fleche.append([i,j])
    
    
    """
    #profondeur
    Fleche = [] 
    
    sommet_initiale = 0
    sommet_verification = False
    while not sommet_verification:
        for fleche_potentiel in M[sommet_initiale]:
            if fleche_potentiel != inf:
                sommet_verification = True
                
    def recursive_profondeur(M, sommet, visite=None):
        if visite is None:
            visite = []
        if sommet not in visite:
            visite.append(sommet)
        
        pasVisite = []
        for el in M[sommet]:
            if el not in visite:
                pasVisite.append(el)
        for sommet in pasVisite:
            recursive_profondeur(M, sommet, visite)
        return visite
    
    Fleche = recursive_profondeur(M, sommet_initiale)
    """
    #Récupération des sommets et création d'un tableau qui contient toutes les infos
    Sommet = []
    for i in range(n):
        #Si c'est le point de départ il est initialisé autrement que les autres
        if d == i:
            Sommet.append([i, 0, i])
        #tout les autres points
        else:
            Sommet.append([i, inf, None])
    
    #Tant qu'il y a eu un changement dans la précédente boucle et qu'on a fat moins de n iteration
    while changement and iteration <= (n-1):
        #On le met a faux comme ça s'il n'y pas de changement on sors de la boucle
        changement = False
        
        #pour chaque flèche
        for element in Fleche:
            #Correspond a la somme du sommet de départ + le poids de l'arête (la flèche)
            calcul = Sommet[element[0]][1] + M[element[0]][element[1]]
            if calcul < Sommet[element[1]][1]:
                #On donne un nouveau poid pour le sommet
                Sommet[element[1]][1] = calcul
                #On change le sommet duquel il provient
                Sommet[element[1]][2] = element[0]
                #On met changement a True ce qui nous fera faire au moins une autre boucle après
                changement = True
                
        #Incrémentation de l'itération
        iteration += 1
        
    #Permet de faire l'affiche des résultat de l'algorithme
    for el in Sommet:
        #Pour tout les sommets qui ne sont pas celui de départ
        if el[0] != d:
            #Si iteration = n alors ça veut dire qu'il y a un cycle a poids négatif
            if iteration == n:
                print(nomNoeuds[el[0]], ": sommet joignable depuis ", nomNoeuds[d],
                      "par un chemin dans le graphe G, mais pas de plus court chemin (présence d'un cycle négatif).")
            #Si un sommet a toujours pour valeur inf ou (et ça va ensemble) il ne provient d'aucun sommet alors il est injoignable
            elif el[1] == inf or el[2] == None:
                print(nomNoeuds[el[0]], ": sommet non joignable depuis ", nomNoeuds[d],
                      "par un chemin dans le graphe G.")
            else:
                #Création d'une liste qui va contenir le chemin du départ vers la destination
                Liste = []
                Liste.append(nomNoeuds[el[0]])
                sommet_suivant = Sommet[el[0]][2]
                
                #Si le dernier sommet ajouté a la liste et le sommet de départ alors on a finit de retracer le chemin 
                while Liste[-1] != nomNoeuds[d]:
                    #On ajoute les noms des sommets et non leur indices dans la liste des noms
                    Liste.append(nomNoeuds[sommet_suivant])
                    #Permet de recalculer le sommet suivant
                    sommet_suivant = Sommet[sommet_suivant][2]
                    
                #Affichage avec tout les éléments
                print(nomNoeuds[el[0]]," : chemin ", Liste[::-1], " et de poids ", el[1])
                
    #met en rouge sur le graphe le chemin du plus court chemin entre le départ et la dernière arrivé parmis les sommets
    #red_edges = chemin_en_rouge(Liste[::-1])
    red_edges = []


def parcoursLargeurMatrice(M, s):
    n = len(M)
    couleur = {}
    
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[s] = 'vert'
    file = [s]
    Resultat = [s]
    
    while file != []:
        i = file[0] #On prend le premier terme de la file
        for j in range(n): #On enfile les successeurs de i encore blancs
            if (M[file[0]][j]==1 and couleur[j]=='blanc'):
                file.append(j)
                couleur[j]='vert' #On les colorie en vert (sommet visités)
                Resultat.append(j) #On les place dans la liste Résultat
        file.pop(0) #On défile i
    return(Resultat)

def parcoursProfondeurMatrice(M, s):
    n = len(M) #taille du tableau
    couleur = {} 
    
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[s] = 'vert'
    pile = [s]
    Resultat = [s]
    
    while pile != []: #Tant que la pile n'est pas vide
        i = pile[-1] #Oon prend le denrier élément de la pile
        Succ_blanc = [] #on crée la liste des ses successeurs non déhà visités
        for j in range(n): #On enfile les successeurs de i encore blancs
            if (M[i][j]==1 and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc != []:
            v = Succ_blanc[0] #On prend le premier
            couleur[v] = 'vert' #On le colorie en vert
            pile.append(v) #On l'empile
            Resultat.append(v) #on e met en resultat
        else:
            pile.pop() #on sort i de la pile
    return(Resultat)

#Programme principal
def main():
    global G
    """
    Permet de générer une matrice que vous donnez directement dans la fonction
    Si vous voulez utiliser une matrice aléatoire avec 50% de flèches ou alors une proportion
    p de flèche, il vous suffit de mettre en commentaire l'appel de la fonction creation_matrice()
    et d'enlever le commentaire de la fonction souhaité.
    """
    creation_matrice()
    #graphe(6,5,20)
    #graphe2(30, 0.3, 0, 50)
    
    print(adjacencePoids)
    
    print()
    print("Bellman-Ford")
    Bellman_Ford(adjacencePoids, 0)
    
    print()
    print("Dijkstra")
    dijkstra(adjacencePoids, 0)
    
    G = nx.DiGraph()
    nombre_lignes, nombre_colonnes = adjacencePoids.shape
        
    #Parcours des lignes et colonnes
    for i in range(nombre_colonnes):
        for j in range(nombre_lignes):
            
            #Si le poid du chemin n'est pas infinit alors le chemin existe
            if adjacencePoids[i][j] != inf:
                
                # Récupère le nom du noeuds
                a,b = choix_nom_noeuds(i, j)
                #Ajout du chemin de i vers j
                G.add_edge(a, b, weight=adjacencePoids[i][j])
    
    #Créer un dictionnaire contenant les étiquettes des arêtes pour le graph
    edge_labels = dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    
    #définition du chemin surligné en rouge sur le graph (modifier les sommets entre les parenthèses)
    #red_edges = chemin_en_rouge([])
    
    #Assigne a chaque arête sa couleur en fonction des conditions
    edge_colors = ['black' if edge in G.edges and edge not in red_edges else 'red' for edge in G.edges]
    
    """
    il est possible que le graphique ne soit pas trop lisible si le nombre de noeuds
    est trop élevé. Parfois certains noeuds peuvent se chevocher ou alors certains poids
    ne sont pas visible. Dans ce cas veuillez tester d'autres formes de graph que vous trouverez
    ci-dessous, sous la forme : "pos = nx.<le nom de la configuration>_layout(G)"
    Certaines de ces configurations peuvent agraver la visibilité. Pensez à mettre en commentaire
    l'ancienne ligne de code avec un '#' ou trois guillement avant et apres la ligne
    La pluspart du temps, les chemins qui font une boucle donc qui ont pour départ leur arrivé
    sont très mal représenté, le seul moyen trouvé et de rajouter un grand nombre de chemins (*3 comparé a avant)
    ce qui rend le graph très brouillon.
    """
    pos = nx.circular_layout(G)
    #pos = nx.random_layout(G)
    #pos = nx.spring_layout(G)
    #pos = nx.shell_layout(G)
    #pos = nx.fruchterman_reingold_layout(G)
    
    # Décale légèrement la position des poids sur le graphe pour éviter le chevauchement
    pos_higher = {k: (x + 0.05, y + 0.08) for k, (x, y) in pos.items()}
    
    
    # Dessine les arêtes
    nx.draw_networkx_edge_labels(G, pos_higher, edge_labels=edge_labels, font_color='blue')       
    nx.draw(G, pos, node_color='pink', with_labels=True, node_size=1000, edge_color=edge_colors, edge_cmap=plt.cm.Reds, arrowsize=10)               
          
            
main()