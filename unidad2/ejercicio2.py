#utilizando operadores logicos, determina si una cadena de texto introducida por 
#el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 
# es suficiente con mostrar true or false 

cadena = input("introduce una cadena: ")

condiciones = len(cadena) >= 3 and len(cadena) <10

print("la cadena es mayor que 3 y menor o igual a 10? ", condiciones)