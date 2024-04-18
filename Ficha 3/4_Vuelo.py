# Carga de datos
partida = input("Ingresa el horario de partida (formato hh:mm: ")
llegada = input("Ingresa el horario de llegada (formato hh:mm): ")

# Procesos
#Transformamos las horas de partida a numero
hp = partida[0] + partida[1]
hora_partida = int(hp)

#Transformamos los minutos de partida a numero
mp = partida[3] + partida[4]
minuto_partida = int(mp)

# Lo mismo pero con lo de llegada
hl = llegada[0] + llegada[1]
hora_llegada = int(hl)

ml = llegada[3] + llegada[4]
minuto_llegada = int(ml)

# Transformamos las horas en minutos y lo sumamos a la variable minuto_partida
minuto_partida += hora_partida * 60
# Hacemos lo mismo con la llegada
minuto_llegada += hora_llegada * 60

# Calculamos
duracion_viaje_min = minuto_llegada - minuto_partida
hora_llegada_hotel = (minuto_llegada + 45) // 60
min_llegada_hotel = (minuto_llegada + 45) % 60

# muestra en pantalla
print(f"La duracion del viaje es de: {duracion_viaje_min} min")
print(f"Llega a las {hora_llegada_hotel}:{min_llegada_hotel}")

