import random

PALOS = ('Basto', 'Oro', 'Espada', 'Copa')
NUMEROS = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

#Generamos las caratas al azar
numero1 = random.choice(NUMEROS)
palo1 = random.choice(PALOS)
numero2 = random.choice(NUMEROS)
palo2 = random.choice(PALOS)
numero3 = random.choice(NUMEROS)
palo3 = random.choice(PALOS)

#Imprimimos las cartas generadas
print("Cartas: ")
print(f'{numero1} de {palo1}')
print(f'{numero2} de {palo2}')
print(f'{numero3} de {palo3}')

#Realizo una variable que almacena si existe el as de espada
es_as1 = numero1 == 1 and palo1 == 'Espada'
es_as2 = numero2 == 1 and palo2 == 'Espada'
es_as3 = numero3 == 1 and palo3 == 'Espada'

#Proceso para ver si existe el as de espadas en el mazo
if es_as1 or es_as2 or es_as3:
    print('El as de espadas esta en la mano.')

#Verificamos si las cartas son del mismo palo
if palo1 == palo2 == palo3:
    #En caso de ser iguales, buscamos la mayor y guardamos en la variable e imprimimos
    cartamayor = max(numero1, numero2, numero3)
    print(f'La carta mas grande es {cartamayor}')
else:
    print('Las 3 cartas no son iguales')
