class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)

    def __str__(self):
        print(
            "{} lanzada en {} con una duracion de {} minutos".format(
                self.titulo, self.lanzamiento, self.duracion
            )
        )

    def __len__(self):
        print(self.duracion)


p = Pelicula("El padrino", "175", "1972")

