from tkinter import *


def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()


def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()


def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


# configuracion de la raiz
root = Tk()
root.config(bd=20)

n1 = StringVar()
n2 = StringVar()
r = StringVar()
Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()  # primer numero
Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()  # segundo numero
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()  # resultado
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Restar", command=restar).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


# Finalmente bucle de la aplicacion
root.mainloop()
