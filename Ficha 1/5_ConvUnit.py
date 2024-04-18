# Carga de datos
pies = float(input("Ingrese una medida en pies: "))

# Desarrollo
yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

# Mostramos en pantalla
print(f'pies -> yardas = {yardas}, pies -> pulgadas = {pulgadas}, pies -> centimetros = {centimetros}, pies -> metros = {metros}')