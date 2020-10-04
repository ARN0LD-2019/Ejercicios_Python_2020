# Realiza una funcion llamada area_rectangulo() que devuelva el area del cuadrado a partir de una base
# y una altura. Calcula el area de un rectangulo de 15 de base y 10 de altura


def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado


rectangulo = area_rectangulo(base=15, altura=10)
print("el area del rectangulo es de: ", rectangulo)

print("##################################")
print("OPCION 2")


def area_cuadrado(base, altura):
    return base * altura


print("la opcion 2 del calculo de el area es de: ", area_cuadrado(15, 10))

