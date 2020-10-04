# FUNCIONES DECORADORAS
# una funcion decoradora es una funcion que envuelve la ejecucion de otra funcion y permite
# extender su comportamiento. Estan pensadas para reutilizarlas gracias a una sintaxis de ejecucion
# mucho mas simple

# EJEMPLO: para crear una funcion decoradora tenemos que recibir la funcion a ejecutar, y envolver
# su ejecucion con el codigo a extender.
# def hola():
#    print("hola!")


# def adios():
#    print("adios!")


def monitorizar(funcion):
    def decorar():
        print("\t* Se esta a punto de ejecutar la funcion:", funcion.__name__)

        funcion()
        print("\t* Se ha finalizado de ejecutar la funcion:", function.__name__)

    return decorar


def adios():
    print("Adios!")

