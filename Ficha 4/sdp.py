#Solicitamos la carga de datos
n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))
n3 = int(input("Ingresa un numero: "))

#Realizamos la operacion de la suma
suma = n1 + n2 + n3

#Desarrollamos el problema
if suma > 10:
    resultado = suma // 2
    print(f'La suma de los 3 numeros es mayor a 10 y el resultado es {resultado}')
else:
    resultado = suma ** 3
    print(f"La suma dio menor a 10 y el resultado es {resultado}")