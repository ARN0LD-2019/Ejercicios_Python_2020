import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("esriba un valor entre [1,9][1,9]")
        print("ejemplo tablas.py")
    else:
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end="")
else:
    print("error: escriba un valor entre [0, 9] [0, 9]")
    print("ejemplo tablas.py")

