#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict, List, Union


class Graph:

    """
    Constructeur pour la classe graphe
    """

    def __init__(self, oriente: bool = False):
        self.graph: Dict[Union[str, int], List[str, int]] = {}
        self.oriente = oriente  # graphe orienté ou non

    """
    Ajoute un sommet au graphe
    """

    def add_node(self, node: Union[str, int]):
        self.graph[node] = []  # ajouter un sommet initialisé à vide

    """
    Ajouter plusieurs sommets en meme temps
    :param nodes: liste des sommets à ajouter
    """

    def add_nodes(self, nodes: List[Union[str, int]]):
        for node in nodes:
            self.add_node(node)

    """
    Ajouter un arete
    Orientation:
        - true: ajouter node2 dans node1 et vise versa
        - false: ajouter node2 dans node1 
    """

    def add_edge(self, node1: Union[str, int], node2: Union[str, int]):

        # Vérifier l'exsitence des sommets
        if node1 not in self.graph:
            self.add_node(node1)  # ajouter node1 si existe pas
        if node2 not in self.graph:
            self.add_node(node2)  # ajouter node2 si existe pas

        # Ajouter l'arete
        self.graph[node1].append(node2)

        # Pour les graphes non orienté
        if not self.oriente:
            self.graph[node2].append(node1)

    """
    Ajouter plusieurs aretes
    :param edges : liste des aretes à ajouter sous forme de tableau 2D
    """

    def add_edges(self, edges: List[List[Union[str, int]]]):
        # Vérifier que chaque edge comporte un paire
        for edge in edges:
            if len(edge) != 2:
                raise ValueError("L'arete doit etre un paire de noeuds")
            self.add_edge(edge[0], edge[1])

    """
    Supprimer un sommet du graphe
    """

    def remove_node(self, node: Union[str, int]):
        # verif de l'existence du sommet
        if node not in self.graph:
            raise ValueError(f"{node} n'existe pas dans le graphe")

        del self.graph[node]  # supprimer le node

        for vertex in list(self.graph.keys()):
            if node in self.graph[vertex]:
                self.graph[vertex].remove(node)  # supp les autres liaisons

    """
    Supprimer plusieurs sommets
    """

    def remove_nodes(self, nodes: List[Union[str, int]]):
        for node in nodes:
            self.remove_node(node)

    """
    Supprimer un arete
    """

    def remove_edge(self, node1: Union[str, int], node2: Union[str, int]):
        if node1 not in self.graph or node2 not in self.graph:
            raise ValueError("Le node doit etre un element du graphe")

        if node2 in self.graph[node1]:
            # enlever node2 des voisins de node1
            self.graph[node1].remove(node2)
        if node1 in self.graph[node2]:
            # enlever node1 des voisins de node2
            self.graph[node2].remove(node1)

    """
    Supprimer plusieurs aretes
    :param edges_to_del: liste 
    """

    def remove_edges(self, edges_to_del: List[List[Union[str, int]]]):
        # Vérifier que chaque edge comporte un paire
        for edge in edges_to_del:
            if len(edge) != 2:
                raise ValueError("L'arete doit etre un paire de noeuds")

            self.remove_edge(edge[0], edge[1])
            
    """
    Affichage de la liste d'adjacence'
    """
    def display(self):
        print("\n")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")
        
        print("\n")

# main project
m_graph = Graph()
m_graph.add_node('A')
m_graph.add_nodes(['B', 'C', 'D', 'E', 'F'])

m_graph.add_edges([['B', 'F'], ['A', 'E'], ['A', 'F']])

m_graph.display()
