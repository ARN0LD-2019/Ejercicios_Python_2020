class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindros):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindros = cilindros

    def __str__(self):
        return "color {}, {} km/h, {} ruedas {} cc".format(
            self.color, self.velocidad, self.ruedas, self.cilindros
        )


C = Coche("azul", 150, 4, 1200)
print(C)

print("#####################################################################")
# Para evitar escribir codigo innecesario, podemos utilizar un truco que consiste en llamar
# el metodo de la superclase y luego simplemente escribir el codigo de la clase:

