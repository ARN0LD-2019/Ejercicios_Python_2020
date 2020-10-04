import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 1 or numero > 9999:
        print("error al ingresar valor ")
        print("ejemplo: descomposicion.py [1- 9999]")
    else:
        # logica
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud - 1 - i]) * 10 ** i))

else:
    print("error al ingresar valor ")
    print("ejemplo: descomposicion.py [1- 9999]")

