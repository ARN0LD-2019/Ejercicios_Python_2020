personajes = []
p = {"nombre": "tiabini", "clase": "princesa", "raza": "humano"}
personajes.append(p)
# print(personajes)
p = {"nombre": "elfo", "clase": "media", "raza": "medio elfo"}
personajes.append(p)
# print(personajes)
p = {"nombre": "diablo", "clase": "pequeño", "raza": "infierno"}
personajes.append(p)
# print(personajes)
for p in personajes:
    print(p["nombre"], p["raza"])

