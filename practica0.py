from math import sqrt


def max(a, b):
    if (a >= b):
        return a
    else:
        return b


def max_de_tres(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= c):
        return b
    else:
        return c


def largo(elemento):
    return len(elemento)


def mdpmqels_for(a, b):
    multiplos = list()
    for i in range(a, b):
        if(i % a == 0):
            multiplos += [i]
    return multiplos


def mdpmqels_while(a, b):
    multiplos = list()
    i = 1
    c = a*i
    while(c < b):
        multiplos += [c]
        i = i+1
        c = a*i
    return multiplos


def es_primo(a):
    raiz = sqrt(a)
    for i in range(2, int(raiz)+1):
        if(a % i == 0):
            return False
    return True


def imprimos(e):
    for i in range(2, e):
        if(es_primo(i)):
            print(i)


def es_potencia_de_dos(a):
    return a % 2 == 0


def potencias_dos_entre(a, b):
    for i in range(a+1, b):
        if(es_potencia_de_dos(i)):
            print(i)


def duplicado(lista):
    largo = len(lista)
    for i in range(largo):
        for x in range(i+1, largo):
            if(lista[x] == lista[i]):
                return True
    return False


def elimina_duplicado(lista):
    largo = len(lista)
    i = 0
    while(i < largo):
        indices = list()
        for x in range(i+1, largo):
            if(lista[x] == lista[i]):
                indices += [x]
        k = len(indices)-1
        while(k >= 0):
            lista = lista[0:indices[k]] + lista[indices[k]+1:largo]
            largo -= 1
            k -= 1
        i += 1
    return lista


def cantidad_nodup(lista):
    copia = lista[:]
    copia = elimina_duplicado(copia)
    return len(copia)


def cant_vocal(cadena):
    vocales = [0, 0, 0, 0, 0]
    for i in range(len(cadena)):
        if(ord(cadena[i]) == 97 or ord(cadena[i]) == 65):
            vocales[0] += 1
        elif(ord(cadena[i]) == 101 or ord(cadena[i]) == 69):
            vocales[1] += 1
        elif(ord(cadena[i]) == 105 or ord(cadena[i]) == 73):
            vocales[2] += 1
        elif(ord(cadena[i]) == 111 or ord(cadena[i]) == 79):
            vocales[3] += 1
        elif(ord(cadena[i]) == 117 or ord(cadena[i]) == 85):
            vocales[4] += 1
    return vocales


def cant_cinco(palabras):
    array = palabras.split()
    cant = 0
    for x in array:
        if len(x) > 5:
            cant += 1
    return cant


# / Represento el timepo en tuplas (HH:MM)
# / Donde HH es un valor entre 0 y 23 y MM entre 0 y 59

def crea_horas(hora, minutos):
    return ((hora+int(minutos/60)) % 24, minutos % 60)


def suma_horas(hora1, hora2):
    nuevahora = (hora1[0]+hora2[0], hora1[1]+hora2[1])
    return ((nuevahora[0]+int(nuevahora[1]/60)) % 24, nuevahora[1] % 60)


print(suma_horas(crea_horas(70, 45), crea_horas(100, 30)))
