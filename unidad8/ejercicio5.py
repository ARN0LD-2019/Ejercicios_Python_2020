class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

    p = peliculas("El padrino", 175, 1972)
    c = Catalogo([p])
    c.mostrar()

