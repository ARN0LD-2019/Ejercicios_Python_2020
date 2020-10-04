# crear un script llamado tabla.py que realice las siguientes
# tareas:
# debe tomar dos argumentos ambos numeros enteros positivos del 1 al 9 sin mostrar un error
# el primer argumento tendra referencia a las filas d euna tabla el segundo a las columnas
# en caso de no recibir uno o ambos argumentos, debe mostrar informacion hacerca de como utilizar el script
# el script contendra el bucle for que tiene el numero de veces del primer argumento
# dentro del for añade un segundo for que tiene el numero de veces del primer argumento
# dentro de segundo for ejecuta una instruccion print ("*", end=''),(end evita el salto de linea )
# ejecuta el codigo y observa el resultao
import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error, filas o columnas incorrectas")
        print("Ejemplo Tabla.py [1-9] [1-9]")
    else:
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" f ", end=" ")


else:
    print("Error, filas o columnas incorrectas")
    print("Ejemplo Tabla.py [1-9] [1-9]")
