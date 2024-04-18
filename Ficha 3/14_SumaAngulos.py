# Carga de datos
print("Ingrese el angulo1")
gradosa1 = int(input("Ingrese los grados: "))
mina1 = int(input("Ingrese los min: "))
sega1 = int(input("Ingrese los seg: "))

print("Ingrese el angulo2")
gradosa2 = int(input("Ingrese los grados: "))
mina2 = int(input("Ingrese los min: "))
sega2 = int(input("Ingrese los seg: "))

# Desarrollo
# Todo a segundos
suma_seg_a1 = sega1 + mina1 * 60 + gradosa1 * 3600
print(f"La suma de todo en segundos del angulo 1 es de: {suma_seg_a1}")
suma_seg_a2 = sega2 + mina2 * 60 + gradosa2 * 3600
print(f"La suma de todo en segundos del angulo 2 es de: {suma_seg_a2}")

#  Ahora hacemos la suma de todo, seria la suma de los 2 angulos
suma_total = suma_seg_a1 + suma_seg_a2

# Pasamos a formato grado:min:seg
g = divmod(suma_total, 3600) # Divido el total de todo, por 3600 que son los segundos que hay en 1 grado
grados_total = g[0]
resto = g[1]
# Ahora, sacamos los minutos pero esta vez dividimos por 60, ya que en 1 min hay 60 seg
m = divmod(resto, 60)
min_total = m[0]
seg_total = m[1]

# Entonces ahora imprimimos en pantalla
print(f"La suma de los dos angulos da como resultado el angulo que vale: {grados_total}g {min_total}' {seg_total}'' ")



