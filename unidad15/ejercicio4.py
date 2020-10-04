# FUNCIONES DECORADAS
# en python dentro de una funcion se pueden definir otras funciones. con la peculiaridad de que
# el ambito de estas funciones se encuentre unicamente dentro de la funcion padre.
# Ambito GLOBAL Y LOCAL
# si utilizamos una funcion reservada locals() obtendremos un diccionario con todas las
# definiciones dentro del espacio local del bloque en el que estamos:


def hola():
    def bienvenido():
        return "Hola!"

    print(locals())  # Mostramso el ambito local


hola()

