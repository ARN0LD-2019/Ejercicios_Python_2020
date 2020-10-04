try:
    n = float(input("introduce un numero: "))
    5 / n
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un numero")
except ZeroDivisionError:
    print("No se puede dividir el numero por 0")
except Exception as e:
    print("Ha ocurrido un error imprevisto", type(e).__name__)

