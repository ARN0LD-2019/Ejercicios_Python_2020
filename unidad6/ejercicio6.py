# una funcion puede utilizar argumentos indeterminados, python utiliza la funcion *args para indicar
# una serie de argumentos indeterminados


def sumax(*args):
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    return resultado

total = sumax(4, 3, 5, 6, 7, 8, 9)
print(total)

