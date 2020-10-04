from tkinter import *

# Configuracion de la raiz
root = Tk()
"""
# variables dinaicas
texto = StringVar()
texto.set("un nuevo texto")

Label(root, text="hola mundo").pack(anchor="nw")
label = Label(root, text="otra etiqueta")
Label(root, text="utlima etiqueta").pack(anchor="se")


label.pack(anchor="center")
label.config(bg="grey", fg="yellow", font=("Verdana", 24))
label.config(textvariable=texto)
# Finalmente bucle de la aplicacion
"""
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")
root.mainloop()
