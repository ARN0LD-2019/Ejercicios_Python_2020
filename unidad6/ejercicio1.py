# se define con la palabra reservada def, el nombre de la funcion y un parentesis que tambien se usa
# para hacer la llamada
# Ejemplo:
print("")


def saludar():
    print("este es la estructura de def")


saludar()
print("##################################")

# Ejemplo de la funcion tabla del 5 con ciclo for


def tabla_del_5():
    for i in range(11):
        print("5 * {} = {}".format(i, i * 5))


tabla_del_5()

print("##################################")

# tabla del 6
def tabla_del_6():
    for i in range(11):
        print("6 * {} = {}".format(i, i * 6))


tabla_del_6()
print("###################################")
# Sin embargo una variable declarada fuera de la funcion (AL MISMO NIVEL) si que es accesible
# desde la funcion
m = 10


def test():
    print(m)


test()
print("###################################")
# sin embargo una varible declarada en una funcion no exite en la funcion principal
def test():
    n = 12


test()
# print(n)
print("###################################")
# Siempre que declaremos la variable antes de la ejecucuion, podremos acceder a ella desde dentro
def test():
    print(l)


l = 9999

test()

# Por lo tanto no podemos modificar una variable externa dentro de una funcion:
def test():
    o = 5  # variable que solo existe dentro de la funcion
    print(o)


o = 10  # variable externa no modificable
test()
print(o)
print("###############################")
print("INSTRUCCION GLOBAL")


def test():
    global o  # variable que hace referencia a la o externa
    o = 5
    print(o)


# al momento de imprimir la instruccion final se muestra la variale global o
o = 10
test()
print(o)

