import random
#Generamos los dados y mostramos en pantalla
d1 = random.randint(1,6)
d2 = random.randint(1, 6)
print(f'Dado 1 = {d1}, Dado 2 = {d2}')

if d1 == d2 or (d1+d2) % 2 != 0:
    print("Ganaste")
else:
    print("Gané yo")