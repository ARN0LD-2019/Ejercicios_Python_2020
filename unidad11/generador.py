import random
import math

# EL OBJETIVO DE ESTE EJERCICIO ES PRACTICAR LA REUTILIZACION DE CODIGO Y LOS MODULOS RANDOM Y MATH
# Nota: Recuerda que el redondeo tradicional round() no requiere ningun modulo.
################################################################################################################
# Crea un script llamado genarador.py que cumpla las siguientes necesidades:
# debe incluir una funcion llamada leer_numero(). Esta funcion tomara 3 valores: (InI, fin  y mensaje).
# El objetivo es leer por pantalla un numero >= que InI y <= que fin. Ademas a la hora de hacer la lectura se mostrara
# en el input el mensaje enviado a una funcion. Finalmente se devolvera el valor. Esta funcion tiene que devolver un numero
# y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no
# sea un numero del InI al fin)
def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error: valor o valido")
        else:
            if valor >= ini and valor <= fin:
                break

    return valor


####################################################################################################
# una vez la tengas creada deberas crear una nueva funcion llamada generador. no recibira ningun parametro
# dentro leeras dos numeros con la funcion leer_numero()
# El primer numero sera llamado numeros, debera ser entre 1 y 20 ambos incluidos y se mostrara el mensaje
# ¿Cuantos numeros quieres generar?[1-20]:
# El segundo numero sera llamado nodo y requerira un numero entre 1 y 3 ambos incluidos. El mensaje que
# mostrara sera: ¿Como quieres redondear los numeros?[1]Al alza [2]A la baja [3] Normal:
def generador():
    numeros = leer_numero(1, 20, "¿Cuantos numeros quieres generar? [1-20]")
    modo = leer_numero(
        1, 3, "¿Como quieres redondear los numeros? [1]Al alza [2]A la baja [3]Normal"
    )
    # Una vez sepas los numeros a geerar y como redondearlos, tendras que realizar lo siguiente:
    # Generar una lista de numeros aleatorios decimales entre 0 y 100 con tantos numeros como el usuario
    # haya indicado
    # A cada uno de esos 100 numeros deberas redondearlos en funcion de lo que el usuario ha especificado en el
    # modo
    # Para cada numero muestra durante el redondeo: el numero normal y despues del redondeo
    # finalmente devolveras la lista de numeros redondeados

    lista = []
    for i in range(numeros):
        numero = random.uniform(0, 101)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            numero = math.ceil(numero)
        elif modo == 2:
            print("{} => {}".format(numero, math.floor(numero)))
            numero = math.floor(numero)
        elif modo == 3:
            print("{} => {}".format(numero, round(numero)))
            numero = round(numero)
        lista.append(numero)

    return lista


generador()

