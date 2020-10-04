from tkinter import *
from tkinter import messagebox as Messagebox

# Configuracion de la raiz
root = Tk()


def test():
    # Messagebox.showinfo("Hola", "Hola Mundo")
    # Messagebox.showwarning("Alerta", "COVID-19")
    # Messagebox.showerror("Error", "Ah ocurrido un error")
    #  resultado = Messagebox.askquestion(
    #    "Salir", "¿Estas seguro que quieres salir sin guardar?"
    # )
    # if resultado == "yes":
    #   root.destroy()
    # resultado = Messagebox.askokcancel("Salir", "¿Sobrescribir el fichero actual?")
    # if resultado:
    #   root.destroy()
    # resultado = Messagebox.askyesno(
    #   "Salir", "¿Estas seguro que quieres salir sin guardar?"
    # )
    # if resultado:
    #   root.destroy()
    #resultado = Messagebox.askretrycancel("Reintentar", "no se puede conectar")
    #if resultado:
    #    root.destroy()


Button(root, text="cliqueame", command=test).pack()

# finalmente bucle de la aplicacion
root.mainloop()

