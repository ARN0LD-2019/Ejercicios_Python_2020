# realiza una funcion llamada agregar_una_vez() que recibe una lista y un elemento. La funcion debe
# añadir al elemento al final de la lista con la condicion de no repetir ningun elemento. Ademas
# si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes
# capturar y mostrar este mensaje en su lugar:
# Error: imposible añadir elementos duplicados   => [elemento]

elementos = [1, 2, 3, 4, 5, 6, 7, 8, -9]


def agregar_una_vez(lista, ele):
    try:
        if ele in lista:
            raise ValueError
        else:
            lista.append(ele)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados => {}".format(ele))


print(elementos)
agregar_una_vez(elementos, 2)
agregar_una_vez(elementos, "hola")
agregar_una_vez(elementos, -9)
print(elementos)

