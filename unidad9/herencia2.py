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
# print(a)


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCION\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(
            self.referencia,
            self.nombre,
            self.pvp,
            self.descripcion,
            self.productor,
            self.distribuidor,
        )


al = Alimento(4321, "alimento1", 543, "caldo de murcielago")
al.productor = "Los olivos"
al.distribuidor = "el gordo"

print(al)

