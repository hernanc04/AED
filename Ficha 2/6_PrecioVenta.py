# Carga de datos
precio = float(input("Ingrese el precio del articulo: "))

# Desarrollo
contado = precio - precio *0.10
tarjeta = precio + precio * 0.05

# Muestra en pantalla
print(f'El precio al contado es de ${contado}')
print(f'El precio pagando con tarjeta es de ${tarjeta}')