# Solicitamos los datos
cuadro1 = int(input("Ingrese el año del primer cuadro: "))
cuadro2 = int(input("Ingrese el año del segundo cuadro: "))
cuadro3 = int(input("Ingrese el año del tercer cuadro: "))

# Verificamos si son anteriores al siglo XX
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    print("Todos los cuadros son anteriores al siglo XX!")
else:
    print("Al menos un cuadro no pertenece al siglo XX")

# Solicitamos el año a comparar
comparar = int(input("Ingresa un año para ver si algun cuadro pertenece al mismo: "))

# Verificamos si existe algun cuadro en el año ingresado
if cuadro1 == comparar or cuadro2 == comparar or cuadro3 == comparar:
    print(f'Uno de los cuadros fue creado en el año {comparar}')
else:
    print(f"Ningun cuadro fue creado en el año {comparar}")

# Realizamos la diferencia entre la mas nueva y la mas vieja
masnueva = max(cuadro1, cuadro2, cuadro3)
masvieja = min(cuadro1, cuadro2, cuadro3)

diferencia = masnueva - masvieja

print(f'La diferencia entre la obra mas nueva y mas vieja es de {diferencia} años')