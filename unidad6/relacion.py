# realiza una funcion llamada relacion que a partir de dos numeros cumpla lo siguiente:
# si el primer numero es mayor que el segundo debe devolver: 1
# si el primer numero es menor que el segundo debe devolver: -1
# si ambos numeros son iguales: debe devolver un 0
# Compruebe la relacion entre los numeros: '5 y 10', '10 y 5', '5 y 5'


def relacion(n1, n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0


print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))

