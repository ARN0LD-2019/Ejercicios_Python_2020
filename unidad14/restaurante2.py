# En este ejercicios debes crear una interfaz gráfica con tkinter (menu.py) que muestre de forma elegante
# el menú del restaurante.

# Tú eliges el nombre del restaurante y el precio del menú, así como las tipografías, colores, adornos y
# tamaño de la ventana.
# El único requisito es que el programa se conectará a la base de datos para buscar la lista categorías y
# platos.
import sqlite3
from tkinter import *

# Configuracion de la raiz

root = Tk()
root.title("Bar el Polges - Menu")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")

Label(
    root,
    text=" Bar el Polges",
    fg="darkgreen",
    font=("Times New Roman", 28, "bold italic"),
).pack()
Label(
    root, text="Menu del dia", fg="green", font=("Times New Roman", 24, "bold italic")
).pack()

Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(
        root, text=categoria[1], fg="black", font=("Tmes New Roman", 20, "bold italic")
    ).pack()

platos = cursor.execute(
    "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])
).fetchall()
for plato in platos:
    Label(root, text=plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()
Label(root, text="").pack()
conexion.close()
Label(
    root,
    text="12 euros (IVA incl.)",
    fg="darkgreen",
    font=("Time New Roman", 20, "bold italic"),
).pack(side="right")
root.mainloop()

