# Carga de datos
nombre_empleado = input("Ingrese su nombre: ")
area_perteneciente = input("Ingrese el area a la que pertenece: ")
salario_actual = float(input("Ingrese el salario que posee actualmente: "))

# Procesos
aumento = salario_actual * 0.08
descuento = salario_actual * 0.025
nuevo_salario = salario_actual + aumento - descuento

# Muestra en pantalla
print(f'Nombre de empleado: {nombre_empleado}')
print(f'Área funcional: {area_perteneciente}')
print(f'Salario actual: ${salario_actual}')
print(f'Nuevo salario: ${nuevo_salario}')