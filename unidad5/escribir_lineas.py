# modulo sys retorna una lista con todos los argumentos pasados por línea de comandos.
# Al ejecutar pyth
import sys

# importamos la libreria del sistema
texto = sys.argv[1]
# la varible texto va a ocupar el segundo espacio y lo va a mostrar por pantalla
# con sys.argv[1]
repeticiones = int(sys.argv[2])
# la varible repeticiones le esta indicando al  interprete que
# en un valor int indique una cantidad y esta sera ubicada en el espacio 2
for r in range(repeticiones):
    print(texto)
# en esta parte le esta indicando que por cada r = numero de "repeticiones"
# imprima texto el numero de veces de r

