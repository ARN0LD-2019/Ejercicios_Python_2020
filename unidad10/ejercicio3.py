# diccionarios
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
colores["amarillo"]
print(colores["amarillo"])
print(colores.get("amarillo", "no se encuentra"))
print("amarillo" in colores)
print(colores.keys())
print(colores.items())
for c in colores:
    print(colores[c])
print("##############################")
for c, v in colores.items():
    print(c, v)
print("##############################")
print(colores.pop("amarillo", "no se ha encontrado"))
print(colores)
colores2 = {"white": "blanco", "black": "negro", "grey": "gris", "purple": "morado"}
print(colores2)
colores2.clear()
print(colores2)

