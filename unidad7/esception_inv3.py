def otra_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error personalizado")
    except ValueError:
        print("Error, no se permite un valor nulo (DESDE LA EXCEPCION)")


otra_funcion()
