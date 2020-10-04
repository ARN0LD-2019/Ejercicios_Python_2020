print("menu iteractivo !!!")
while True:
    print(
        """Selecciona una opcion:
    1) saludar
    2) sumar dos numeros
    3 despedia"""
    )
    opcion = input()
    if opcion == "1":
        print("hola")
    elif opcion == "2":
        n1 = float(input("introduce el primer numero: "))
        n2 = float(input("introduce el segundo numero: "))
        print("BITCH!!!")
        print("la suma es de: ", n1 + n2)
    elif opcion == "3":
        print("goodbye!!!")
    break
else:
    print("opcion no valida")
