#! /usr/bin/python

# 2da Practica Laboratorio
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario.
# Ejemplo: {'A':1, 'B':2, 'C':1} (Nodos A y C pertenecen al conjunto
# identificado con 1, B al identificado on 2)

grafo_lista = (['A', 'B', 'C', 'D', 'E', 'F', 'G'], [
               ('A', 'B'), ('B', 'C'), ('A', 'B'), ('C', 'D'), ('E', 'F')])


def make_set(lista):
    '''
    Inicializa una lista de vértices de modo que cada uno de sus elementos pasen a ser conjuntos unitarios.
    Retorna un disjointSet.
    '''
    conjunto = {}
    for i in range(len(lista)):
        conjunto[lista[i]] = i
    return conjunto


def find(elem, disjoint_set):
    '''
    Obtiene el identificador del conjunto de vértices al que pertenece el elemento.
    '''
    return disjoint_set[elem]


def union(id_1, id_2, disjoint_set):
    '''
    Dado dos identificadores de conjuntos de vértices, une dichos conjuntos.
    Retorna la estructura actualizada
    '''
    for x, y in disjoint_set.items():
        if y == id_2:
            disjoint_set[x] = id_1
    return disjoint_set


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo:
        Entrada: [['a','b','c','d'], [('a', 'b')]]
        Salida: [['a, 'b'], ['c'], ['d']]
    '''
    disjoint_set = make_set(grafo_lista[0])
    for i in grafo_lista[1]:
        clave1 = i[0]
        clave2 = i[1]
        union(find(clave1, disjoint_set), find(
            clave2, disjoint_set), disjoint_set)
    joint_set = dict()
    for k, y in disjoint_set.items():
        if y in joint_set:
            joint_set[y] += [k]
        else:
            joint_set[y] = [k]
    devuelvo = list()
    for h in joint_set:
        devuelvo += [joint_set[h]]
    return devuelvo


def main():
    print(componentes_conexas(grafo_lista))


if __name__ == '__main__':
    main()
