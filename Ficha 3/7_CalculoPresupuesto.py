# Carga de datos
presupuesto = float(input("Ingrese el presupuesto para el hospital: "))

# Procesos
presupuesto_urgencias = presupuesto * 0.37
presupuesto_pediatria = presupuesto * 0.42
presupuesto_traumatologia = presupuesto * 0.21

# Muestra de datos
print(f'Lo que recibirá el área de urgencias es de: ${presupuesto_urgencias}')
print(f'Lo que recibirá el área de pediatria es de: ${presupuesto_pediatria}')
print(f'Lo que recibirá el área de traumatologia es de: ${presupuesto_traumatologia}')