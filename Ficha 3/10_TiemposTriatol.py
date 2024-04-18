# Carga de datos
tiempo_nat = input("Ingresa el tiempo en mm:ss logrado en natacion: ")
tiempo_bici = input("Ingresa el tiempo en mm:ss logrado en ciclismo: ")
tiempo_ped = input("Ingresa el tiempo en mm:ss logrado en pedestre: ")

# Procesos
# Pasamos los min a segundos y transformamos la cadena a int
nat_seg = int(tiempo_nat[0] + tiempo_nat[1]) * 60 + int( tiempo_nat[3] + tiempo_nat[4] )
bici_seg = int(tiempo_bici[0] + tiempo_bici[1]) * 60 + int( tiempo_bici[3] + tiempo_bici[4] )
ped_seg = int(tiempo_ped[0] + tiempo_ped[1]) * 60 + int( tiempo_ped[3] + tiempo_ped[4] )

# Realizamos la suma de todos los segundos
total_segundos = nat_seg + bici_seg + ped_seg

# Calculamos las horas en total utilizando la funcion divmod
horas = divmod(total_segundos, 3600) # Esto me devuelve (hora, segundos) una tupla
total_h = horas[0] # Por eso acá, ponemos horas[0], para que seleccione la hora de la tupla de arriba

# Calculada las horas con divmod, sacamos ahora minutos y segundos con la misma funcion
minutos = divmod(horas[1], 60)  # Acá divide la otra parte de la tupla, los segundos de residuo por 60, para sacar los minutos (min, seg)
total_m = minutos[0]
total_s = minutos[1]

# Ya tenemos el primer punto, asi q procedemos a imprimir en pantalla
print(f'El tiempo total de la prueba fue de {total_h}hs:{total_m}min:{total_s}seg')

# Calculamos el maximo y minimo en segundos e imprimimos
maximo_seg = max(nat_seg, bici_seg, ped_seg)
minimo_seg = min(nat_seg, bici_seg, ped_seg)
print(f'El tiempo maximo en segundos es de: {maximo_seg}')
print(f'El tiempo minimo en segundos es de: {minimo_seg}')

# Hacemos el promedio de la prueba e imprimimos
promedio = (total_segundos) / 3
promedio = round(promedio, 2)
print(f"El tiempo promedio es de {promedio}")
