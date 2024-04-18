# Datos
monto_base = float(input("Ingrese el precio: "))
km = float(input("Cantidad de KM a recorrer: "))
kmadicional = 0.30

# Procesos
adicional = kmadicional * km
costo_final = monto_base + adicional

# Muestra de resultados
print(f"El costo del viaje es {costo_final}")

