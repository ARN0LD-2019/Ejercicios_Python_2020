# Para evitarnos escribir codigo innecesario, podemos utilizar un truco que
# consiste en llaar al metodo de la superclase y luego simplemente escribir el
# codigo de la clase


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindros):
        super().__init__(
            color, ruedas
        )  # utilizamos super() sin self en lugar de vehiculo
        self.velocidad = velocidad
        self.cilindros = cilindros

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindros
        )


c = Coche("azul", 4, 120, 6)
print(c)

