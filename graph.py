#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict, List, Union

class Graph:
    
    """
    Constructeur pour la classe graphe
    """
    def __init__(self, oriente: bool):
        self.graph: Dict[Union[str, int], List[str, int]] = {}
        self.oriente = oriente # graphe orienté ou non
       
        
       
    """
    Ajoute un sommet au graphe
    """
    def add_node(self, node: Union[str, int]):
        self.graph[node] = [] # ajouter un sommet initialisé à vide
       
        
       
    """
    Ajouter un arete
    Orientation:
        - true: ajouter node2 dans node1 et vise versa
        - false: ajouter node2 dans node1 
    """
    def add_edge(self, node1: Union[str, int], node2: Union[str, int]):
        
        # Vérifier l'exsitence des sommets 
        if node1 not in self.graph:
            self.add_node(node1) # ajouter node1 si existe pas
        if node2 not in self.graph:
            self.add_node(node2) # ajouter node2 si existe pas
        
        # Ajouter l'arete
        self.graph[node1].append(node2)
        
        # Pour les graphes non orienté
        if not self.oriente:
            self.graph[node2].append(node1)
        