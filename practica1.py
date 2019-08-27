# ! /usr/bin/python

# 1ra Practica Laboratorio
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys


def lee_grafo_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada:
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno:
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    i = -1
    k = 0
    vertices = list()
    aristas = list()
    for line in sys.stdin:
        if i == -1:
            i = int(line)
        elif k < i:
            vertices += [line[:-1]]
            k += 1
        else:
            sep = line.rstrip().split()
            aristas += [(sep[0], sep[1])]
    return (vertices, aristas)


def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada:
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno:
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    vertices = list()
    aristas = list()
    with open(file_path, "r") as file:
        lines = file.readlines()
        i = int(lines[0])
        for x in range(1, i):
            vertices += [lines[x].rstrip()]
        for k in range(i, len(lines)):
            sep = lines[k].rstrip().split()
            aristas += [(sep[0], sep[1])]
    return (vertices, aristas)


def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    print(len(grafo[0]))
    for i in grafo[0]:
        print(i)
    for x, y in grafo[1]:
        print(x + " " + y)


def lista_a_incidencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion
    en matriz de incidencia.
    '''
    matriz = list()
    v = len(grafo_lista[0])
    for x, y in grafo_lista[1]:
        fila = [0] * v
        indice0 = grafo_lista[0].index(x)
        indice1 = grafo_lista[0].index(y)
        fila[indice0] = 1
        fila[indice1] = 1
        matriz += [fila]
    return grafo_lista[0], matriz


def incidencia_a_lista(grafo_incidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    aristas = list()
    vertices = grafo_incidencia[0]
    for l in grafo_incidencia[1]:
        i = l.index(1)
        l[i] = 0
        j = l.index(1)
        aristas += [(vertices[i], vertices[j])]
    return vertices, aristas


def imprime_grafo_incidencia(grafo_incidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    size = len(grafo_incidencia[0])
    print(size)
    for i in grafo_incidencia[0]:
        print(i + ' ', end='')
    print()
    for x in grafo_incidencia[1]:
        for j in range(size):
            print(str(x[j])+' ', end='')
        print()


def lista_a_adyacencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
    n = len(grafo_lista[0])
    matriz = [[0 for x in range(n)] for y in range(n)]
    for x, y in grafo_lista[1]:
        i0 = grafo_lista[0].index(x)
        i1 = grafo_lista[0].index(y)
        matriz[i0][i1] = 1
        matriz[i1][i0] = 1
    return grafo_lista[0], matriz


def adyacencia_a_lista(grafo_adyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
    '''
    n = len(grafo_adyacencia[0])
    aristas = list()
    vertices = grafo_adyacencia[0]
    matriz = grafo_adyacencia[1]
    for i in range(n):
        for j in range(i, n):
            if matriz[i][j]:
                aristas += [(vertices[i], vertices[j])]
    return vertices, aristas


def imprime_grafo_adyacencia(grafo_adyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    vertices = grafo_adyacencia[0]
    n = len(vertices)
    matriz = grafo_adyacencia[1]
    print("  ", end='')
    for i in vertices:
        print(i + ' ', end='')
    print()
    for i in range(n):
        print(vertices[i]+' ', end='')
        for j in range(n):
            print(str(matriz[i][j])+' ', end='')
        print()


# FIN EJERCICIO PRACTICA #################### EJMEPLOS PROFESORA
grafo_adyacencia1 = (
    ['A', 'B', 'C', 'D'],
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], ]
)

grafo_adyacencia2 = (
    ['A', 'B', 'C', 'D'],
    [[0, 2, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], ]
)


def lee_entrada_1():
    count = 0
    for line in sys.stdin:
        count = count + 1
        print('Linea: [{0}]'.format(line))
    print('leidas {0} lineas'.format(count))


def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print('Linea: [{0}]'.format(line))
    except EOFError:
        pass

    print('leidas {0} lineas'.format(count))


def lee_archivo(file_path):
    print('leyendo archivo: {0}'.format(file_path))
    count = 0

    with open(file_path, 'r') as f:
        first_line = f.readline()
        print('primer linea: [{}]'.format(first_line))
        for line in f:
            count = count + 1
            # print 'Linea: [{0}]'.format(line)
    print('leidas {0} lineas'.format(count))


def main():
    imprime_grafo_adyacencia(grafo_adyacencia1)
    print()
    imprime_grafo_adyacencia(grafo_adyacencia2)


if __name__ == '__main__':
    main()
