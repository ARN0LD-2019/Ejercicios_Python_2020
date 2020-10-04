# Realiza un programa que lea  dos numeros por teclado y permita elegir entre
# 3 opciones  en un menu:
# mostrar una suma de dos numeros
# mostrar una resta de los dos numeros (el primero menos e segundo)
# mostrar una multiplicacion de los dos numeros
# en caso de no introducir una opcon valida el programa informa que no es correcta

print("menu de ejercicio while")
while True:
    print(
        """¿Que quieres hacer?
    1) Sumar  dos numeros
    2) restar dos numeros
    3) multiplicar dos numeros"""
    )
    opcion = input()
    if opcion == "1":
        n1 = float(input("introduce el primer numero: "))
        n2 = float(input("introduce el segundo numero: "))
        suma = n1 + n2
        print("el resultado es: ", suma)
    elif opcion == "2":
        n1 = float(input("introduce el primer numero: "))
        n2 = float(input("introduce el segundo numero: "))
        resta = n1 - n2
        print("el resultado es: ", resta)
    elif opcion == "3":
        n1 = float(input("introduce el primer numero: "))
        n2 = float(input("introduce el segundo numero: "))
        multiplicacion = n1 * n2
        print("el resultado es: ", multiplicacion)
    break
else:
    print("opcion no valida")

