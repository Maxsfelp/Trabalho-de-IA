#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Missionários e Canibais
Autores: Felipe Maxusel / Humberto Bianchini
"""


def main():
    # Formato = [Missionario, Canibais, Margem]
    possibilidades = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
    # estado_final = [0, 0, 0]
    ja_visitados = [[3, 3, 1]]
    estado_atual = [[3, 3, 1]]
    print(verifica_estado(possibilidades, estado_atual, ja_visitados))
    print(ja_visitados)


def verifica_estado(p, e, jv):
    novos_estados = []
    for i in range(len(p)):  # 0 - 1 - 2 - 3 - 4
        for j in range(len(e)):  # 0 - 1
            estado = []
            for k in range(len(e[j])):  # 0 - 1 - 3
                tmp = e[j][k] - p[i][k]
                estado.append(tmp)
            if 3 >= estado[1] <= estado[0] <= 3 and estado not in jv:
                novos_estados.append(estado)
                jv.append(estado)
    return novos_estados


if __name__ == '__main__':
    main()
