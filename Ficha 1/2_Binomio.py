# Solicitamos los datos
a = int(input("Ingresa el valor para a: "))
b = int(input("Ingresa el valor para b: "))

# Realizamos la operacion
d = (a + b) * (a + b) # Es una forma

e = a**2 + 2*a*b + b**2 #Otra forma

#Imprimimos en pantalla el resultado
print("El resultado de la primera forma es: ", d)
print("El resultado de la segunda forma es: ", e)