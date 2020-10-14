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
    estado_atual = [[3, 3, 1]]
    if estado_final in estado_atual:
        print('nao')
    faixa_estados = verifica_estado(possibilidades, estado_atual)
    print(faixa_estados)


def verifica_estado(possibilidades, estado_atual):
    novos_estados = []
    ja_visitados = [estado_atual]
    for i in range(len(possibilidades)):
        estado = []
        for j in range(len(estado_atual)):
            for k in range(len(estado_atual[j])):
                tmp = estado_atual[j][k] - possibilidades[i][k]
                estado.append(tmp)
        if estado[0] >= estado[1] and estado not in ja_visitados:
            novos_estados.append(estado)
            ja_visitados.append(estado)
    return novos_estados


if __name__ == '__main__':
    main()
