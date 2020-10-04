from collections import deque

cola = deque(["Hector", "Juan", "Miguel"])
print(cola)
cola.append("maria")
cola.append("el yoni")
p = cola.popleft()
print(cola)
