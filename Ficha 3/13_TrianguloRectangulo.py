# Carga de datos
c1 = float(input("Ingrese el valor del primer cateto: "))
c2 = float(input("Ingrese el valor del segundo cateto: "))

# Procesos
hip = (c1 ** 2 + c2 ** 2)**0.5
hip = round(hip, 2)
# Calculamos valor de lado mayor y menor
val_max = max(c1, c2)
val_min = min(c1, c2)
# Mostramos en pantalla
print(f'La hipotenusa es {hip}\nEl lado mayor vale: {val_max}\nEl lado menor vale: {val_min}')
