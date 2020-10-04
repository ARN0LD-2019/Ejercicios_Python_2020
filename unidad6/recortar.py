# Realiza una funcion llamada recortar que reciba tres parametros.
# El primero es el numero a recortar
# El segundo es el limite inferior
# El tercero el limite superior
# La funcion tendra que cumplir lo Siguiente:
# Devolver el limite inferior si el numero es menor que este
# Devolver el limite superior si el numero es mayor que este
# Devolver el numero sin cambios si no se supera ningun limite


def recortar(numero, inferior, superior):
    if numero < inferior:
        return inferior
    elif numero > superior:
        return superior
    else:
        return numero


print(recortar(15, 0, 10))

