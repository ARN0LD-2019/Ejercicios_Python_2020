from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuracion de la raiz
root = Tk()
# ruta = FileDialog.askopenfilename(
#    title="Abrir un fichero",
#   initialdir="C:",
#  filetypes=(("Ficheros de texto", "*.txt"),),
# )
# print(ruta)
# ruta = FileDialog.asksaveasfile(title="Guardar un fichero")
# print(ruta)
fichero = FileDialog.asksaveasfile(
    title="Guardar un fichero", mode="r+", defaultextension=".txt"
)
if fichero != None:
    fichero.write("hola")
    fichero.close()


# def test():
#   color = ColorChooser.askcolor(title="Elige un color")
#  print(color)


Button(root, text="Cliqueame", command=fichero).pack()


root.mainloop()

