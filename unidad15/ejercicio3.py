# FUNCIONES GENERADAS

numero = []
for numero in [0, 1, 2, 3, 4, 5]:
    if numero % 2 == 0:
        print(numero)


def pares(n):
    for numero in range(n + 1):
        if numero % 2 == 0:
            yield numero


numero = [numero for numero in pares(10)]
print(numero)

