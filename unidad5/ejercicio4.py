# crea un script llamado descomposicion.py que realice las siguientes tareas:
# debe tomar un argumento que sea un numero entero positivo
# en caso de no recibir un argumento debe mostrar informacion acerca de como utilizar
# el script
# El objetivo del script es descomponer el numero en unidades, decenas, centenas, miles..
# tal que por ejemplo  si se introduce el numero:
# 3647
# el programa debera devolver una descomposicion linea a linea como la siguiente utilizando las
# tecnicas de formateo

import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error, numero es incorrecto")
        print("Ejemplo: descomposicion.py [1-9999]")
    else:
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud - 1 - i]) * 10 ** i))

else:
    print("Error, numero es incorrecto")
    print("Ejemplo: descomposicion.py [1-9999]")

