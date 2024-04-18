# Carga de datos
a = int(input("Ingrese el valor para a: "))
b = int(input("Ingrese el valor para b: "))
c = int(input("Ingrese el valor para c: "))
x = int(input("Ingrese el valor del punto X del polinomio: "))

# Desarrollo de operaciones
pol = a*(x**2) + b*x + c
disc = b**2  -  4 * a * c

# Muestra de datos en pantalla
print(f'El valor del polinomio en x = {x}, es de {pol}')
print(f'El valor de su discriminante es de {disc}')