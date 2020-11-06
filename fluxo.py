#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Atividade 5: Fluxo em grafos (Parte 1)
Autor: Humberto Bianchini
"""

import networkx as nx
import sys
ent = sys.argv[1]


def le_arquivo(grafo, dad):
    arquivo = open(ent, "r")  # Abertura do arquivo de entrada
    for linha in arquivo:
        o, d, v = linha.split()
        grafo.add_node(o)
        grafo.add_node(d)
        grafo.add_edge(o, d, weight=v)
        dad[o, d] = v
    arquivo.close()  # Fechamento do arquivo de entrada


def verifica_corte(grafo, dad):
    inverso = []
    for i in list(grafo.edges()):
        for j in list(grafo.edges()):
            if i != j:
                opcao = [(i[0], i[1]), (j[0], j[1])]
                if opcao not in inverso:
                    soma = 0
                    grafo.remove_edge(i[0], i[1])
                    grafo.remove_edge(j[0], j[1])
                    for key, value in dad.items():
                        if key == (i[0], i[1]) or key == (j[0], j[1]):
                            soma += int(value)
                    opcao.reverse()
                    inverso.append(opcao)
                    if not nx.has_path(G, 's', 't'):
                        print(f"Corte: Arestas {i[0]}-{i[1]} e {j[0]}-{j[1]} - Fluxo total: {soma}")
                    grafo.add_edge(i[0], i[1])
                    grafo.add_edge(j[0], j[1])


if __name__ == '__main__':
    dados = {}
    G = nx.DiGraph()
    le_arquivo(G, dados)
    verifica_corte(G, dados)
