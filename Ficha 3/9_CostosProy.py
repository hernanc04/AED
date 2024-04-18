# Carga de datos
presupuesto = float(input("Presupuesto para desarrollo del sistema: "))

# Procesos
ganancia = presupuesto * 0.17
costo_maximo = presupuesto - ganancia #Restamos la ganancia para asegurarnos de que al menos la ganancia minima es del 17%, entonces usamos el resto del presupuesto para el desarrollo

# Muestra de resultados
print(f"Los costos del proyecto no deben exceder los ${costo_maximo}")