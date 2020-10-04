from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.resizable(1, 1)

frame = Frame(root, width=480, height=320)
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="yellow")
root.config(bd=10)
root.config(relief="ridge")

# Ultimo paso
root.mainloop()
