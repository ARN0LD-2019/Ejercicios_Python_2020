from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


# Configuracion de la raiz

root = Tk()
opcion = IntVar()

Radiobutton(root, text="opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="opcion 3", variable=opcion, value=3, command=seleccionar).pack()
monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()
# Finalmente bucle de la aplicacion
root.mainloop()
