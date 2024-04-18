# Datos
perimetro = float(input("Ingrese el perimetro del rectangulo: "))
lado1 = float(input("Ingrese el valor de un lado del rectangulo: "))

# Procesos
lado2  = (perimetro - (2  * lado1))/2
area = lado1 * lado2

# Muestra en pantalla
print(f'El area del rectangulo es {area}')