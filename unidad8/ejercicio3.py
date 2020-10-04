class Galleta:
    chocolate = False

    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}".format(sabor, forma))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta chocolatada")
        else:
            print("soy una galleta sin chocolate")

