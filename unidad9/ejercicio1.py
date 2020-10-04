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


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t{}
        PVP\t\t{}
        DESCRIPCION\t{}
        ISBN\t\t{}
        AUTOR\t\t{}""".format(
            self.referencia,
            self.nombre,
            self.pvp,
            self.descripcion,
            self.isbn,
            self.autor,
        )


li = Libro(999, "los 3 cochinitos", 4323, "cuento para niños")
li.isbn = 6578
li.autor = "pedro picapedra"
print(li)

