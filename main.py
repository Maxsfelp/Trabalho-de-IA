#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Missionários e Canibais
Autores: Felipe Maxsuel / Humberto Bianchini
"""


def main():
    # Formato = [Missionario, Canibais, Margem]
    possibilidades = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
    estado_final = [0, 0, 0]
    ja_visitados = [[3, 3, 1]]
    estado_atual = [[3, 3, 1]]
    while estado_final not in estado_atual:
        estado_atual = verifica_estado(possibilidades, estado_atual, ja_visitados)


def verifica_estado(p, e, jv):
    novos_estados = []
    for i in range(len(p)):
        for j in range(len(e)):
            estado = []
            for k in range(len(e[j])):
                if e[j][2] == 1:
                    tmp = e[j][k] - p[i][k]
                else:
                    tmp = e[j][k] + p[i][k]
                estado.append(tmp)
            if (estado[0] == 3 or estado[0] == estado[1] or estado[0] == 0) and estado not in jv and (0 <= estado[1] <= 3):
                novos_estados.append(estado)
                jv.append(estado)
    print(novos_estados)
    return novos_estados


if __name__ == '__main__':
    main()
