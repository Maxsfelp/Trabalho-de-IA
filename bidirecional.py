#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Missionários e Canibais
Autores: Felipe Maxsuel / Humberto Bianchini
"""


def main():
    # Formato = [Missionarios, Canibais, Margem]
    possibilidades = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
    estado_atual1 = [[3, 3, 1]]
    estado_atual2 = [[0, 0, 0]]
    ja_visitados1 = [[3, 3, 1]]
    ja_visitados2 = [[0, 0, 0]]
    while estado_atual1 != estado_atual2:
        print('Caminho (3, 3, 1): ')
        estado_atual1 = verifica_estado(possibilidades, estado_atual1, ja_visitados1)
        if estado_atual1 == estado_atual2:
            break
        else:
            print('Caminho (0, 0, 0): ')
            estado_atual2 = verifica_estado(possibilidades, estado_atual2, ja_visitados2)


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
            if estado[0] == 3 or estado[0] == estado[1] or estado[0] == 0:
                if estado not in jv and (0 <= estado[1] <= 3):
                    novos_estados.append(estado)
                    jv.append(estado)
    print(novos_estados)
    return novos_estados


if __name__ == '__main__':
    main()
