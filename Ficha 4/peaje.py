import random
# Solicitamos los datos
patente =input("Ingrese los digitos de la patente: ")
ultimo_digito = int(patente[-1])
print(f"El ultimo digito es {ultimo_digito}")
# Sorteamos un numero e imprimimos en pantalla
numero = random.randint(0,9)
print(f'El numero sorteado es el {numero}')

# Vemos si el ultimo digito es igual al numero sorteado
if numero == ultimo_digito:
    tarifa = 50
    print(f'Acertaste el numero, tu tarifa es de {tarifa}')
else:
    tarifa = 90
    print(f'No acertaste el numero, tu tarifa es de {tarifa}')


# Verificamos si el ultimo numero es igual a 7
if ultimo_digito == 7:
    descuento = tarifa - tarifa * 0.50
    print(f"Tu ultimo digito de patente termina en 7, entonces tu tarifa final es de {descuento}")
else:
    descuento = tarifa - tarifa * 0.10
    print(f"Tu ultimo digito de patente no termina en 7, entonces tu tarifa final es de {descuento}")



