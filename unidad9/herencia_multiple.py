class A:
    def __init__(self):
        print("esta es la clase A")


class B:
    def b(self):
        print("esta es la clase B")


class C(B, A):
    def c(self):
        print("esta es la clase C compuesta de la clase A y B")


c = C()

