#realiza un programa que cumpla el siguiente algoritmo utilizando siempre que 
# sea posible operadores de asignacion 
# guardar en una variable numero_magico 12345679 (sin el 8)
# lee por pantalla otro numero_usuario especifica que sea entre 1 y 9 
# multiplica el numero_usuario por 9 en si mismo 
# multiplica el numero magico por el numero usuario en si mismo 
# finalmente muestra el valor final del numero_magico por pantalla 


numero_magico = 12345679

numero_usuario = int(input(" introduce un numero: "))
numero_usuario = numero_usuario * 9
print("el numero usuario multiplicado por 9 es: ", numero_usuario)
numero_magico = numero_usuario * numero_magico
print ("el numero magico multiplicado por el numero usuario es :", numero_magico)