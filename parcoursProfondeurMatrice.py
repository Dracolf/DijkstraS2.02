# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:06:50 2024

@author: MS
"""

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

import numpy as np
M = np.array([[0,0,1,1,0,0,0], [1,0,0,0,1,0,0], [0,1,0,1,0,0,0], [0,0,0,0,1,0,1], [0,0,0,0,0,1,0], [0,0,0,0,1,0,0], [0,1,0,0,0,0,0]])

#POUR CONNEXE CLASSIQUE
#Liste / esemble de tous les sommet [a,b,c,d,e,f]
#parcour en pronfondeur de Liste[0]
#On récupère alors L1
#L = L - L1
#on refait jusqu'à que L soit vide

n = len(M)
Liste = []
for i in range(n):
    L.append(i)

Liste_connexe = []
while len(L) > 0:    

print(parcoursProfondeurMatrice(M,0))