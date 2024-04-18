# Cargamos los datos
med = float(input("Ingresa el valor del medicamento: "))
desc = med * 0.35
preciofinal = med - desc

# Mostramos en pantalla
print(f'El precio inicial del medicamento es {med}, aplicando el descuento de 35% se le restarían {desc} quedando asi el precio final de {preciofinal}')
