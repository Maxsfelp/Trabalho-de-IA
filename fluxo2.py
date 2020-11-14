#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Atividade 6: Fluxo em grafos (Parte 2)
Autor: Humberto Bianchini e Felipe Maxsuel
"""

import networkx as nx
import sys
ent = sys.argv[1]


def le_arquivo(grafo, dad):
    arquivo = open(ent, "r")  # Abertura do arquivo de entrada
    for linha in arquivo:
        o, d, v = linha.split()
        grafo.add_edge(o, d, capacity=int(v))
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
                    opcao.reverse()
                    inverso.append(opcao)
                    if not nx.has_path(G, 's', 't'):
                        for key, value in dad.items():
                            if key == (i[0], i[1]) or key == (j[0], j[1]):
                                soma += int(value)
                        print(f"Corte: Arestas {i[0]}-{i[1]} e {j[0]}-{j[1]} - Fluxo total: {soma}")
                    grafo.add_edge(i[0], i[1], capacity=int(dad[i[0], i[1]]))
                    grafo.add_edge(j[0], j[1], capacity=int(dad[j[0], j[1]]))


if __name__ == '__main__':
    dados = {}
    G = nx.DiGraph()
    le_arquivo(G, dados)
    verifica_corte(G, dados)
    fluxomax, arestasel = nx.maximum_flow(G, 's', 't')
    print(f"\nFluxo máximo do grafo: {fluxomax}, correspondente à capacidade de seu corte mínimo\n")
    for chave, valor in arestasel.items():
        for k in valor:
            print(f"Aresta: {chave}-{k}, fluxo elementar: {valor[k]}")
