# Vehiculo (color, ruedas), Coches (velocidad km/h, cilindrada), bicicleta (urbana, deportiva)
# camioneta (carga kg), motocicleta (velocidad (km/h), cilindros CC)

# Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos
# Realiza una funcion llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando
# el nombre de su clase y atributos
# Modifica la funcion catalogar() para que reciba un argumento optativo RUEDAS haciendo que muestre
# unicamente los que su numero de ruedas concuerde con el valor del argumento ruedas.
# Ponlo a prueba con 0.2 y 4 ruedas como valor


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


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindros, carga):
        super().__init__(
            color, ruedas, velocidad, cilindros
        )  # utilizamos super() sin self en lugar de vehiculo
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg ".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(
            color, ruedas
        )  # utilizamos super() sin self en lugar de vehiculo
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", es de tipo {}  ".format(self.tipo)


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(
            color, ruedas, tipo
        )  # utilizamos super() sin self en lugar de vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ",  {} km/h , {} cc ".format(
            self.velocidad, self.cilindrada
        )


vehiculos = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("roja", 2, "deportiva", 180, 900),
]


def catalogar(lista, ruedas=None):
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print("Se ha encontrado {} vehiculos con {} ruedas".format(contador, ruedas))
    for v in lista:
        if ruedas == None:
            print("{} {}".format(type(v).__name__, v))
        else:
            if v.ruedas == ruedas:
                print("{} {}".format(type(v).__name__, v))


catalogar(vehiculos, 4)
