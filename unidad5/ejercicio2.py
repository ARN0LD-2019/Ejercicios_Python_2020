# formatea los siguientes valores para mostrar el resultado
# "hola mundo alineado a la derecha 20 caracteres"
print("{:>20}".format("hola mundo"))
# hola mundo truncamente en el cuarto caracter(indice 3)
print("{:.3}".format("hola mundo"))
# hola mundo alineado al centro 20 caracteres con truncamiento en el segundo caracter
print("{:^20.1}".format("hola mundo"))
# 150  formateo a 5 numeros enteros rellenados con ceros
print("{:05d}".format(150))
# 7887 formateo a 7 numeros enteros rellenados con espacios
print("{:7d}".format(7887))
# 20.02 formateo a 3 numeros enteros y 3 numeros decimales
print("{:07.3f}".format(20.02))
# el 07 sn los espacios en total "el punto es un espacio por es en ves de 6 se ponen 7"
# se le asigna un punto debido a que dividiremos los enteros de los decimales
