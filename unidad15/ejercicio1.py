lista = []
for a in "casa":
    lista.append(a)
print(lista)
##########################################
# Metodo con comprension de listas
lista = [letra for letra in "casa"]
print(lista)

###############################
# Metodo tradicional
lista = []
for numero in range(0, 11):
    lista.append(numero ** 2)
print(lista)

###########################################
# Metodo con compresion de listas
lista = [numero ** 2 for numero in range(0, 11)]
print(lista)

###########################################
# Multiples de dos entre 0 y 10
lista = []
for numero in range(0, 11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

###########################################
# metodo con compresion de listas
lista = [numero for numero in range(0, 11) if numero % 2 == 0]
print(lista)


###########################################
