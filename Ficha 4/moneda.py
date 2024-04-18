import random
# Generamos la tirada
moneda = random.choice(('cara', 'cruz'))

#Pedimos al usuario que haga la apuesta
apuesta = input("Adivina si es Cara o Cruz: ").lower()

#Verificamos si acertó o no
if apuesta == 'cara' and moneda == 'cara':
    print('Acertaste, ganaste')
elif apuesta == 'cruz' and moneda == 'cruz':
    print('Acertaste, ganaste')
else:
    print('Sos un choto XD')

