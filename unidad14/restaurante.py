import sqlite3

# Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd()
# que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:
# CREATE TABLE categoria(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(100) UNIQUE NOT NULL)
# CREATE TABLE plato(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(100) UNIQUE NOT NULL,
#    categoria_id INTEGER NOT NULL,
#    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
##############################################################################
# Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen,
# lo notarás porque en este caso no usamos el IF NOT EXISTS y eso lanzará un error.
# En caso contrario mostrará que se han creado correctamente.


def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute(
            """
           CREATE TABLE categoria(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nombre VARCHAR(100) UNIQUE NOT NULL)
           """
        )
    except sqlite3.OperationalError:
        print(" La tabla de categorias ya existe")
    else:
        print("la tabla de categorias se ha creado correctamente")
    try:
        cursor.execute(
            """
           CREATE TABLE plato(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nombre VARCHAR(100) UNIQUE NOT NULL, 
           categoria_id INTEGER NOT NULL,
           FOREIGN KEY(categoria_id) REFERENCES categoria(id))
           """
        )
    except sqlite3.OperationalError:
        print(" La tabla de categorias ya existe")
    else:
        print("la tabla de categorias se ha creado correctamente")

    conexion.close()


# Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se
# encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error,
# por que el nombre es UNIQUE).

# Luego crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te
# permita Crear una categoría o Salir. Puedes hacerlo en una función mostrar_menu().
# Añade las siguientes tres categorías utilizando este menú de opciones:

# Primeros
# Segundos
# Postres


def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoria?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe".format(categoria))
    else:
        print("La categoria '{}' fue creada correctamente".format(categoria))

    conexion.commit()
    conexion.close()


# Crea una función llamada agregar_plato() que muestre al usuario las categorías disponibles y
# le permita escoger una (escribiendo un número).

# Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en
# cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

# Agrega la nueva opción al menú de opciones y añade los siguientes platos:

# Primeros: Ensalada del tiempo / Zumo de tomate
# Segundos: Estofado de pescado / Pollo con patatas
# Postres: Flan con nata / Fruta del tiempo


def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir al plato: ")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input(" > "))

    plato = input("¿Nombre de el nuevo plato? \n> ")

    try:
        cursor.execute(
            "INSERT INTO plato VALUES (null, '{}','{}')".format(
                plato, categoria_usuario
            )
        )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe".format(plato))
    else:
        print("El plato '{}' fue creada correctamente".format(plato))

    conexion.commit()
    conexion.close()


# Crea una función llamada mostrar_menu() que muestre el menú con todos los platos
# de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes
# adornar la forma en que muestras el menú por pantalla.


def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute(
            "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])
        ).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))
    conexion.close()


# crear la base de datos
crear_db()
# menu de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante")
    opcion = input(
        "\nIntroduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar menu \n[4] Salir del programa\n\n"
    )

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("nos vemos")
        break
    else:
        print("opcion incorrecta")

