# realiza una funcion llamada area_circulo que devuelva el area de un circulo a partir de un radio. calcula
# el area de un circulo de 5 de ancho
import math

r = float(input("introduce el radio del circulo: "))
area = math.pi * r * r
print("el area del circulo es: ", area)


print("###########################################")
print("SEGUNDO METODO: ")


def area_curculo(radio):
    return (radio ** 2) * math.pi


print(area_curculo(23))

