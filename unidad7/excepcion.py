# Las EXCEPCIONES son bloques de codigo que nos permiten continuar con la ejecucion de un programa
# pese a que ocurra un error
# Bloques TRY-EXCEPT
# Para evitar el fallo debemos poner el codigo propenso a erores en un bloque try y luego encadenar
# un bloque except para tratar la situacion excepcional mostrando que ha ocurrido un fallo

try:
    n = float(input("Introduce un numero: "))
    m = 10
    print("{}/{}={}".format(n, m, n / m))
except:
    print("error al ingresar el numero")

print("#####################################")

while True:
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")

print("#####################################")

while True:
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha salido bastante bien")
    finally:  # se ejecutara halla o no halla una excepcion
        print("Fin de la iteracion")

