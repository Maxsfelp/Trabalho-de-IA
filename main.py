#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Missionários e Canibais
Autores: Felipe Maxuel / Humberto Bianchini
"""

# Formato = [Missionario, Canibais, Margem]
possibilidades = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
estado_final = [0, 0, 0]
estado_atual = [3, 3, 1]
novos_estados = []
ja_visitados = [estado_atual]
for i in range(0, len(possibilidades)):
    tmp = 0
    estado = []
    for j in range(0, len(estado_atual)):
        tmp = estado_atual[j] - possibilidades[i][j]
        estado.append(tmp)
    if estado[0] >= estado[1] and estado not in ja_visitados:
        novos_estados.append(estado)
        ja_visitados.append(estado)
print(novos_estados)
print(ja_visitados)
