# format es un metodo de las cadenas de texto que nos permite formatear informacion en una cadena
# (variables o valores literales) comodamente utilizando identificadores referenciados
c = "{n} - {m} = {r}".format(m=2, r=3 - 2, n=3)
print(c)
# ejemplo 2
ejemplo = "este es un ejemplo"
texto = "¿Que es esto ? R= {} ".format(ejemplo)
print(texto)
# formateo de numeros enteros rellendos con espacios:
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
# formateo de numeros rellenando los espacios vacios con 0
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
# formateo de numeros flotantes rellenados con espacios
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(152.232))
