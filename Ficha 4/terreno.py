# Solicitamos la medida

frente = float(input("Ingrese la medida del frente: "))
fondo = float(input("Ingrese la medida del fondo"))

# Creo una variable para almacenar la superficie
sup = frente * fondo

# Verificamos si es cuadrada o rectangular

if frente == fondo:
    print("El terreno es cuadrado")
else:
    print("El terreno es rectangular")

print(f'La superficie del terreno es de {sup}')