# catalogo de peliculas para usar peristencia utilizando pickle
from io import open
import pickle


class Pelicula:
    # constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(" se ha creado una pelicual", self.titulo)

    def __str__(self):
        return "{} ({})".format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = []
    # constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("el catalogo esta vacio")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open("ejercicio3.pckl", "ab+")
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("el fichero esta vacio")
        finally:
            fichero.close()
        print("se ha cargado {} peliculas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open("ejercicio3.pckl", "wb")
        pickle.dump(self.peliculas, fichero)
        fichero.close()

