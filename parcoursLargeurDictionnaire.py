# -*- coding: utf-8 -*-
"""
Created on Wed May 15 07:42:33 2024

@author: MS
"""

def parcoursdic(G,S):
    #G est un dico
    couleur = dict()
    for x in G:
        couleur[x] = 'blanc'
    P = dict()
    P[S] = None
    couleur[S] = 'gris'
    Q = [S]
    while Q:
        u = Q[0]
        for v in G[u]:
            if couleur[v] == 'blanc':
                P[v] = u
                couleur[v] = 'gris'
                Q.append(v)
            Q.pop(0)
            couleur[u] = 'noir'
    return P