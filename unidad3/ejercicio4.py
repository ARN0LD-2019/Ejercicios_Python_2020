# Realiza un programa que pida al usuario cuantos numeros quiere introducir, luego lee todos
# los numeros y realiza una media aritmtica
numero = int(input("introduce cantidad de numeros: "))
suma = 0
for n in range(numero):
    suma += int(input("introduce numeros: "))
    print(
        "se han introducido",
        numero,
        "la suma total es de: ",
        suma,
        "la media es de: ",
        suma / numero,
    )
