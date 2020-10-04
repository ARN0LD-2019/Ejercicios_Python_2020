# Realiza un programa que lea dos numeros por teclado y determine los siguientes aspectos (es suficiente con 
# mostrar true or false)
#si los dos numeros son iguales 
#si los dos numeros son diferentes 
#si el primero es mayor que el segundo 
#si el segundo es mayor o igual que el primero 

n1 = float(input("introduce el primer numero: "))
n2 = float(input("introduce el segundo numero: "))

print("los numeros son iguales ?", n1 == n2 )
print("si los dos numeros son diferentes? ", n1 != n2)
print("si el primero es mayor que el segundo ?", n1 > n2)
print("si el segundo es mayor o igual que el primero? ", n2 >= n1)