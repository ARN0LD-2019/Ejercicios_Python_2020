# Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa
# se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion:

lista = [1, 2, 3, 4, 5]
try:
    lista = [10]
except IndexError:
    print("el indice que estas buscando no se encuentra")

