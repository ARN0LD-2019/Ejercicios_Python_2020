# Paso de argumentos por nombre, en python no es necesario escribir los argumentos en el orden en que la
# funcion define sus parametros, podemos especificar el nombre del parametro y de esa manera escribir
# los argumentos en cualquier orden
def restar(actual, nacimiento):
    resultado = actual - nacimiento
    return resultado


edad = restar(nacimiento=1994, actual=2020)
print("tu edad es de: ", edad)

