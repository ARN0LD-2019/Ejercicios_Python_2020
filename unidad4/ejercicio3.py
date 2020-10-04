# durante la planificacion de un proyecto se han acordado una lista de tareas
# para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menos es el numero de
# orden, mas prioridad)
# crea una estructura de tipo cola con todas las tareas ordenadas pero SIN LOS NUMEROS DE ORDEN
#
from collections import deque

tareas = [
    [6, "distribucion"],
    [2, "diseño"],
    [1, "concepcion"],
    [7, "mantenimiento"],
    [4, "produccion"],
    [3, "planificacion"],
    [5, "pruebas"],
]
tareas.sort()
cola = deque()
for tarea in tareas:
    cola.append(tarea[1])
for tarea in cola:
    print(tarea)
