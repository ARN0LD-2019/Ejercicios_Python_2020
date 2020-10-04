class Galleta:
    chocolate = False

    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una Galleta {} y {}".format(sabor, forma))

    def chocolatear(self):
        self.chocolate = True


g = Galleta("chocolateada", "rectangular")
print(g)
