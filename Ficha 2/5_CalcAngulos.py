# Carga de datos
x = int(input("Ingresa el valor de X: "))
y = int(input("Ingresa el valor de Y: "))
"""
Tenemos que: 
x = alfa + beta
y = alfa - beta

donde 
x = alfa + beta 
=> alfa = x - beta

por lo tanto

y = alfa - beta
y = x - beta - beta
y = x - 2*beta
y + 2beta = x
2beta = x - y
beta = (x - y)/2

Entonces
si y = alfa - beta
=> alfa = y + beta
"""
beta = (x - y) / 2
alfa1 = x - beta
alfa2 = y + beta

#Mostramos resultados
print(f"El valor del angulo alfa es: {alfa1} y {alfa2}")
print(f'El valor del angulo beta es de {beta}')
