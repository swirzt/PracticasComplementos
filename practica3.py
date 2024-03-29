#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3ra Practica Laboratorio
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

'''
Recordatorio:
- Un camino/ciclo es Euleriano si contiene exactamente 1 vez
a cada arista del grafo
- Un camino/ciclo es Hamiltoniano si contiene exactamente 1 vez
a cada vértice del grafo
'''


def esCaminoEuleriano(grafo, camino):
    """Comprueba si una lista de aristas constituye un camino euleriano
    en un grafo.

    Argumentos:
        grafo: Grafo en formato de listas.
               Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        camino: Lista de aristas. Posible camino.
                Ej: [('a', 'b), ('b', 'c')]

    Retorno:
        boolean: camino es camino euleriano en grafo

    """
    largoCamino = len(camino)
    if len(grafo[1]) > largoCamino:
        return 0  # El camino es más corto que la cantidad de aristas
    for e in range(largoCamino):
        x = camino[e][0]
        y = camino[e][1]
        estaEnGrafo = 0
        for i, j in grafo[1]:
            if i == x and j == y:
                estaEnGrafo = 1
        if estaEnGrafo == 0:
            return False  # La arista no esta en grafo
        if e < largoCamino-1 and y != camino[e+1][0]:
            return False  # No es un camino
        for p in range(e+1, largoCamino):
            x1 = camino[p][0]
            y1 = camino[p][1]
            if x == x1 and y == y1:
                return False  # Repite aristas
    return True


def esCicloEuleriano(grafo, ciclo):
    """Comprueba si una lista de aristas constituye un ciclo euleriano
        en un grafo.

        Argumentos:
                grafo: Grafo en formato de listas.
                           Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

                camino: Lista de aristas. Posible ciclo.
                                Ej: [('a', 'b), ('b', 'c')]

    Retorno:
        boolean: ciclo es ciclo euleriano en grafo

    """
    if len(ciclo) == 0:
        if grafo[1] == []:
            return True
        else:
            return False
    if esCaminoEuleriano(grafo, ciclo):
        if ciclo[len(ciclo)-1][1] == ciclo[0][0]:
            return True
    return False


def esCaminoHamiltoniano(grafo, camino):
    """
    Comprueba si una lista de aristas constituye un camino hamiltoniano en un grafo.

    Argumentos:
    -grafo: Grafo en formato de listas.
    Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])
    -camino: Lista de aristas. Posible camino.
    Ej: [('a', 'b), ('b', 'c')]

    Retorno:
    -boolean: camino es camino hamiltoniano en grafo
    """
    cantV =  len(grafo[0])
    largoCamino = len(camino)
    if cantV == 1:
        if camino == grafo[1] and largoCamino != 0:
            return True
        return False
    vertices = [0] * cantV
    if largoCamino < cantV-1:
        return False  # Un camino hamiltoniano tiene n-1 aristas y un ciclo tiene n
    for e in range(largoCamino):
        x = camino[e][0]
        y = camino[e][1]
        if not x in grafo[0] or not y in grafo[0]:
            return False
        vertices[grafo[0].index(x)] += 1
        vertices[grafo[0].index(y)] += 1
        if x == y:
            return False  # Utiliza un lazo
        estaEnGrafo = 0
        for i, j in grafo[1]:
            if i == x and j == y:
                estaEnGrafo = 1
        if estaEnGrafo == 0:
            return False  # La arista no esta en grafo
        if e < largoCamino-1 and y != camino[e+1][0]:
            return False  # No es un camino
        for p in range(e+2, largoCamino):
            x1 = camino[p][0]
            y1 = camino[p][1]
            if x == x1 or y == y1:
                return False  # Repite vértices
    for p in vertices:
        if p > 2 or p == 0:
            return False
    return True


def esCicloHamiltoniano(grafo, ciclo):
    """Comprueba si una lista de aristas constituye un ciclo hamiltoniano
    en un grafo.

    Argumentos:
            grafo: Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

            camino: Lista de aristas. Posible ciclo.
                            Ej: [('a', 'b), ('b', 'c')]

Retorno:
    boolean: ciclo es ciclo hamiltoniano en grafo

"""
    if len(ciclo) == 0:
        if grafo[0] == []:
            return True
        else:
            return False
    if esCaminoHamiltoniano(grafo, ciclo):
        if ciclo[len(ciclo)-1][1] == ciclo[0][0]:
            return True
    return False


def tieneCaminoEuleriano(grafo):
    """Comprueba si un grafo no dirigido tiene un camino euleriano.

    Argumentos:
            grafo: Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Retorno:
            boolean: grafo tiene un camino euleriano

"""
    v = len(grafo[0])
    grados = [0 for x in range(v)]
    for x in range(v):
        for t,z in grafo[1]:
            if t == grafo[0][x]:
                grados[x] += 1
            if z == grafo[0][x]:
                grados[x] += 1
    impares = 0
    for k in grados:
        if k%2 == 1:
            impares += 1
    if impares == 0 or impares == 2:
        return True
    return False


def cicloEuleriano(grafo):
    """Obtiene un ciclo euleriano en un grafo no dirigido, si es posible

    Argumentos:
        grafo: Grafo en formato de listas.
                Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Retorno:
        lista de aristas: ciclo euleriano, si existe
        None: si no existe un camino euleriano
    """

    # Sugerencia: Usar el Algoritmo de Fleury
    # Recursos:
    # http://caminoseuler.blogspot.com.ar/p/algoritmo-leury.html
    # http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/

    v = len(grafo[0])
    aristas = grafo[1]
    grados = [0 for x in range(v)]
    for x in range(v):
        for t,z in grafo[1]:
            if t == grafo[0][x]:
                grados[x] += 1
            if z == grafo[0][x]:
                grados[x] += 1
    impares = 0
    for k in grados:
        if k%2 == 1:
            impares += 1
    if impares != 0:
        return None
    ciclo = [aristas[0]]
    aristas.remove(aristas[0])





def main():
    cicloEuleriano((['a', 'b', 'c', 'd'], [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]))


if __name__ == '__main__':
    main()
