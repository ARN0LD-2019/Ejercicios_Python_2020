# Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se
# bloquee y ademas explica en un mensaje al usuario la cusa y/o solucion

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre 0")

