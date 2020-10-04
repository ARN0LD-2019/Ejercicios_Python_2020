# crea un conjunto llamado usuarios con los usuarios maria, david, elvira, juan y marcos
usuarios = {"maria", "david", "elvira", "juan", "marcos"}
# crea un conjunto llamado administradores con los administradores juan y marta
administradores = {"juan", "marta"}
# borra el administrador juan del conjunto de administradores
administradores.discard("juan")
# añade a marcos como el nuevo adminsitrador pero no lo borres del conjunto de usuarios
administradores.add("marcos")
# muestra todos los usuarios por pantalla de forma dinamica, ademas debes indicar si
# cada usuario es administrador
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "es usuario")

