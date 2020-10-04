import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute("UPDATE usuarios SET nombre='Pikachu', edad=255 WHERE dni='123456'")
cursor.execute("DELETE FROM usuarios WHERE dni='654321'")
# cursor.execute("DELETE FROM usuarios") elimina todos los campos de la tabla usuarios
# usuario = cursor.fetchall()
# print(usuario)
conexion.commit()
conexion.close()

