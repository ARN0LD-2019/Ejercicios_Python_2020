class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCION\t{}""".format(
            self.referencia, self.nombre, self.pvp, self.descripcion
        )


class Adorno(Producto):
    pass


a = Adorno(1234, "adorno1", 25, "vasos chidos")
print(a)
