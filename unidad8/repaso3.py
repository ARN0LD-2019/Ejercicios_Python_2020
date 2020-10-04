class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

    def __del__(self):
        print("se ha borrado la pelicula {}".format(self.titulo))

    def __str__(self):
        return "Se ha creado la pelicula {} que tiene duracion de: {} minutos y  en el año: {}".format(
            self.titulo, self.duracion, self.lanzamiento
        )

    def __len__(self):
        return self.duracion


p = Pelicula("Guerra de los Mundos", 203, 2005)
str(p)
print(p)

