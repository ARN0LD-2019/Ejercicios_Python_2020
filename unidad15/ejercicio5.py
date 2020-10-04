# Como vemos se nos muestra un diccionario, aqui encontraremos la funcion bienvenido()
lista = [1, 2, 3]


def hola():
    numero = 50

    def Bienvenido():
        return "Hola!"

    print(locals())  # Mostramos el ambito local


hola()
# Como se puede observar, ahora ademas de la funcion tenemos una clave con el numero y el
# valor 50. Sin embargo no encontramos la lista, pues esta se encuentra fuera del ambito local.
# de hecho se encuentra en el ambito global, el cual podemos mostrar con la funcion reservada globals()

