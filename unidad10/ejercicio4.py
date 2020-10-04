# crea una funcion modificar () que a partir de una lista de numeros realice las
# siguientes tareas sin modificar la original

# borrar los elementos duplicados
# ordenar la lista de mayor a menor
# eliminar todos los numeros impares
# realizar la suma de todos los numeros que quedan
# añadir como primer elemento de la lista la suma realizada
# devolver la lista modificada
# finalmente despues de ejecutar la funcion comprueba que la suma de todos los numeros a partir del segundo
# concuerden con el primer numero de la lista tal que asi:
# nueva_lista = modificar_lista(lista)
# print(nueva_lista[0] == sum(nueva_lista[1:]))
# True

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]


def modificar(l):
    l = list(
        set(l)
    )  # Cuando se manda un conjunto en un metodo set se eliminan los elementos duplicados
    l.sort(reverse=True)  # Metodo sort Reverse ordena la lista de mayor a menor
    for i, n in enumerate(l):  # Elimina los numeros impares
        if n % 2 != 0:
            del l[1]
    suma = sum(l)  # sumar todos los elementos de la lista
    l.insert(
        0, suma
    )  # el resultado de la suma se va a insertar en la poscion 0 de lista
    return l  # se tiene que retornar la lista para mostrar los cambios


nueva_lista = modificar(
    lista
)  # se declaran todas las operaciones de la fucion modificar

print(
    nueva_lista[0] == sum(nueva_lista[1:])
)  # la suma de todos los valores de la lista deben estar en el principio

