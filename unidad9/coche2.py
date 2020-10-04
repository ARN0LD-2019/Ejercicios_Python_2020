class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindros):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindros = cilindros

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindros
        )


c = Coche("azul", 4, 150, 1200)
print(c)
