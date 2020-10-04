import pickle

# clase de prueba
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# creamos la lista de los nombres con los objetos
nombres = ["pedro", "pica", "piedra"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)
# Escribimos la lista en el fichero con pickle
f = open("personas.pckl", "wb")
pickle.dump(personas, f)
f.close()

# leemos la lista del fichero con pickle
f = open("personas.pckl", "rb")
personas = pickle.load(f)

f.close()

for p in personas:
    print(p)
