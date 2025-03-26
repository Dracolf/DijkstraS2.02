# -*- coding: utf-8 -*-
"""
Created on Wed May 15 07:46:17 2024

@author: MS
"""

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

import numpy as np
M = np.array([[0,0,1,1,0,0,0], [1,0,0,0,1,0,0], [0,1,0,1,0,0,0], [0,0,0,0,1,0,1], [0,0,0,0,0,1,0], [0,0,0,0,1,0,0], [0,1,0,0,0,0,0]])

print(parcoursLargeurMatrice(M,0))