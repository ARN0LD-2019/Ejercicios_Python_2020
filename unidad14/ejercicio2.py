import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()


# cursor.execute(
#    """
# CREATE TABLE usuarios(
# dni VARCHAR(9) PRIMARY KEY,
# nombre VARCHAR(100),
# edad INTEGER,
# email VARCHAR(100)
# )
# """
# )

# usuarios = [
#    ("123456", "Mario", 51, "mario@ejemplo.com"),
#    ("654321", "Mercedes", 38, "mercedes@ejemplo.com"),
#    ("987654", "Juan", 19, "juan@ejemplo.com"),
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute(
#   """
# CREATE TABLE productos (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(100) NOT NULL,
#   marca VARCHAR(50) NOT NULL,
#   precio FLOAT NOT NULL
# )
# """
# )

# producto = [("Teclado", "Logitech", 19.95), ("raton", "sumitel", 100.00)]

# cursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)", producto)

# cursor.execute("SELECT * FROM productos")

# productos = cursor.fetchall()
# for producto in productos:
#    print(producto)


cursor.execute(
    """
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR(9) UNIQUE,
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
)
"""
)

usuarios = [
    ("123456", "Mario", 51, "mario@ejemplo.com"),
    ("654321", "Mercedes", 38, "mercedes@ejemplo.com"),
    ("987654", "Juan", 19, "juan@ejemplo.com"),
]
cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

conexion.commit()
conexion.close()

