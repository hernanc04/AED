# Datos
vfavor = int(input("Ingresa la cantidad de votos a favor: "))
vcontra = int(input("Ingresa la cantidad de votos en contra: "))

# Desarrollo
total_votos = vfavor + vcontra
porcentajefavor = (vfavor / total_votos) * 100
porcentajecontra = (vcontra / total_votos) * 100

# Muestra en pantalla
print(f'El porcentaje de votos a favor es de {porcentajefavor}% y el porcentaje de votos en contra es de {porcentajecontra}%')