import random

array = []
suma = 0

for i in range(10):
    elemento = random.randint(1, 50)
    array.append(elemento)
    suma += elemento

print(f'''Suma de todos los elementos
Arreglo: {array}
Suma: {suma}''')