# Metodos especiales
class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

        # Destruccion de clase

        def _del_(self):
            print("Se esta borrando la pelicula", self.titulo)

        # Redefinimos el metodo string
        def _str_(self):
            return "{} lanzada en {} con una duracion de {} minutos".format(
                self.titulo, self.lanzamiento, self.duracion
            )

        # Redefinimos el metodo lenght
        def _len_(self):
            return self.duracion
            p = Pelicula("El padrino", 175, 1972)
            print(len(p))
