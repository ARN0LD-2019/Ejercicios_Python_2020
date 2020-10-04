class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha crado una pelicula", self.titulo)

    def __del__(self):
        print("Se ha borrado la pelicula", self.titulo)


p = Pelicula("Los pitufos", 143, 2001)
del p

