# Realiza un programa que pida al usuario escribir un numero del 0 al 9
# en dado caso de que no lo escriba repetir el ciclo
numeros = [1, 3, 6, 9]
while True:
    numero = int(input("digite un numero del 0 al 9: "))
    # if numero >= 0 and numero <= 9:
    #   print("bien hecho")
    #  break
    if numero in numeros:
        print("el numero", numero, "se encuentra en la lista", numeros)
    else:
        print("el numero", numero, "NO se encuentra en la lista", numeros)
    break

