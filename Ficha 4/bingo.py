import random
# Generamos los numeros aleatorios
tarjeta_bingo = random.sample(range(1,100), 15)
#print(f'Los numeros de la tarjeta son: {tarjeta_bingo}')

# Solicitamos al usuario que ingrese 3 numeros enteros
n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))

# Verificamos si algun numero está en el la tarjeta
if (n1 in tarjeta_bingo) or (n2 in tarjeta_bingo) or (n3 in tarjeta_bingo):
    print("El jugador marcó algún número de la tarjeta")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")