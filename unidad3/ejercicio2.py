# realiza un programa que lea un numero impar por teclado,
# si el usuario no introduce un numero impar, debe repetirse el proceso
# hasta que lo introduzca correctamente

numero = 0
while numero % 2 == 0:
    numero = int(input("introduce un numero inpar: "))

