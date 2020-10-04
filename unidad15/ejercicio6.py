lista = [1, 2, 3, 4, 5, 6]


def hola():
    numero = 50

    def bienvenido():
        return "Hola!"

    print(globals().keys())  # Mostrar el ambito global
    # comando para acceder a una clave declarada con anterioridad en este ejemplo llamaremos a lista
    print(globals()["lista"])


hola()
# Como podemos observar desde el ambito global tenemos acceso a muchas mas definiciones porque engloba
# a su vez todas las de sus bloques padres.

