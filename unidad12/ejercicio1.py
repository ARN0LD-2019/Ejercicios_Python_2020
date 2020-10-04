# pickle: libreria para guardar ficheros
import pickle

# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Escritura en modo binario, vacía el fichero si existe
fichero = open("lista.pckl", "wb")
# Escribe la colección en el fichero
pickle.dump(lista, fichero)

fichero.close()

del fichero
# Lectura en modo binario
fichero = open("lista.pckl", "rb")
# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
print(lista_fichero)

