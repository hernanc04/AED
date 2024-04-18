# Ingresamos los datos
emin = int(input("Ingresa la edad minima establecida"))
edad1 = int(input("Ingresa la primera edad: "))
edad2 = int(input("Ingresa la segunda edad: "))
edad3 = int(input("Ingresa la tercera edad: "))

# Verificamos si cumplen la edad
cumple_edad = edad1 >= emin and edad2 >= emin and edad3 >= emin

if cumple_edad:
    print("Todos cumplen con la edad minima establecida.")
else:
    print("No pueden pasar. ")