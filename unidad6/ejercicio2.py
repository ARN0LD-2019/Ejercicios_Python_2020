# Para comunicarse con el exterior, las funciones pueden devolver valores al proceso principal gracias
# a la instruccion return
def test():
    return "esto es un retorno", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2345422


# Los valores devueltos se tratan como valores literales directos del tipo de dato retornado
# por ejemplo no podemos sumar una cade con un numero: ej c = test() + 12345
print(test())
print("##########################")
# Tambien podemos devolver cualquier tipo de coleccion y manejarla directamente:
def test():
    return 1, 2, 3, 4, 5, 6, 7, 8, 9


test()
print(test())
print(test()[-1])
print(test()[4:-1])

# es posible asignar el valor retornado a una variable

print("###########################")
lista = test()
print(lista[4])
