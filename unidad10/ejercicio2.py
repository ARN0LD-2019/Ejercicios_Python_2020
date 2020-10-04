# se puede generar una lista desde la siguiente estructura
lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(6)
print(lista)
# el metodo count te muestra la cantidad x de elementos en  tu lista
lista2 = ["hola mundo", "hola marte", "hola jupiter", "hola saturno"].count(
    "hola mundo"
)
print(lista2)
# metodo index te muestra el primer elemento de tu lista
lista3 = ["hola mundo", "hola marte", "hola jupiter", "hola saturno"].index(
    "hola jupiter"
)
print(lista3)

lista4 = list("hola mundo")
lista4.reverse()
print(lista4)


