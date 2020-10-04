# Realiza una funcion separar que tome una lista de numeros enteros y devuelva dos listas ordenadas
# la primera con los numeros pares y la segunda con los numeros impares
ejemplo_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares


pares, impares = separar(ejemplo_lista)
print(pares)
print(impares)

