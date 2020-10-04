# ARGUMENTOS INDETERMINADOS


def indeterminados(*args):
    for arg in args:
        print(arg)


indeterminados(3456, [3, 4, 5, 6, 7, 8, 9], "Kaboom")

print("#######################################")


def palabra_clave(**kwargs):
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


palabra_clave(a="ejemplo1", b="ejemplo2", c=[1, 2, 3, 4, 5, 6, 7, 8, 9])

