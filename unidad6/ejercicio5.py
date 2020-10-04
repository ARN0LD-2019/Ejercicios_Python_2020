# ARGUMENTOS POR DEFAULT
# se puede especificar argumentos por default de moodo que, aunque no se pase el valor corrspondiente
# la funcion la asume por default


def dividir(divisor, dividendo=2):
    # el argumento por default es dividendo = 2
    resultado = divisor / dividendo
    return resultado


# es posible llamar a la funcion  pasandole los dos parametros:
# ejemplo dividir(400, 300) como tambien
# ejemplo2 dividir(400)

ejemplo = dividir(400, 300)
ejemplo2 = dividir(400)
print(ejemplo)
print(ejemplo2)

