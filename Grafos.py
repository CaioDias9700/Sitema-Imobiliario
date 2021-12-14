

"""Um problema de grande aplicabilidade em Grafos é o chamado Problema do Caixeiro Viajante (TSP) , que consiste em
encontrar um ciclo hamiltoniano de custo mínimo. Apesar de sua resolução ser difícil
, por se tratar de um problema NP-completo, ele é usado para modelar e resolver problemas em diversas áreas da ciência."""

"""Desta forma, o TSP visa, a partir de um vértice inicial v0, visitar todos os demais vértices uma única vez, 
voltando para v0, caminhando o mínimo possível"""

"""Um dos algoritmos conhecidos para resolver o TSP é o Twice-Around (T.A), no qual, a partir de um grafo G é 
gerada sua árvore geradora mínima (MST), suas arestas são duplicadas e, então, é encontrado um circuito
euleriano que é base para o ciclo hamiltoniano e suas repetições são eliminadas."""



import networkx as nx
import numpy as np


def Twice_Around(G):
    MST = nx.minimum_spanning_tree(G)
    Sgrafo = nx.MultiGraph()
    for edge in MST.edges():
        Sgrafo.add_edge(edge[0], edge[1], weight = G[edge[0]][edge[1]]['weight'])
        Sgrafo.add_edge(edge[0], edge[1], weight = G[edge[0]][edge[1]]['weight'])

    Inicio = [4]
    Lista = []
    for i in range(0, len(Inicio)):
        Eulirian = nx.eulerian_circuit(Sgrafo, source = Inicio[i])
        Hamilt = []
        for edge in Eulirian:
            if edge[0] not in Hamilt:
                Hamilt.append(edge[0])
            if edge[1] not in Hamilt:
                Hamilt.append(edge[1])

        Hamilt.append(Hamilt[0])
        Peso = 0
        for i in range(0, len(Hamilt)-2):
            Peso = Peso + G.get_edge_data(Hamilt[i], Hamilt[i+1])['weight']

        print("Ciclo Hamiltoniano: ", Hamilt)
        print("Peso: ", Peso)
        Lista.append(Peso)
        Lista.append(Hamilt)
    return Lista
Matriz = np.loadtxt('Matriz.txt')
G = nx.from_numpy_matrix(Matriz)
Lista = Twice_Around(G)