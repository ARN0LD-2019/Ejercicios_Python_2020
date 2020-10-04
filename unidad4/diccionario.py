colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
# imprimir un color en especfico
print(colores["azul"])
# cambiar valores a el diccionario en el ejemplo se cmbia yellow por white
colores["amarillo"] = "white"
print(colores)
numeros = {10: "diez", 20: "veinte", 30: "treinta"}
print(numeros[10])
del colores["amarillo"]
print(colores)
edades = {"hector": 27, "maria": 18, "jose": 20}
print(edades)
# operadores en asignacion aplicado a los diccionarios
edades["hector"] += 1
print(edades["hector"] + edades["maria"])
