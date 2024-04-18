# Datos
# Transformar en centesimas tod, para ello multiplicamos los segundos por 100
espalda = 52*100 + 15
pecho = 62 * 100 + 75
mariposa = 59 * 100 + 80
libre = 48 * 100 + 15

#Procesos
total = espalda + pecho + mariposa + libre
# Tenemos que 1 min = 60 seg, 1 seg = 100 cts => 1 min = 60 seg * 100cts = 6000cts
min = divmod(total,6000)
min_total = min[0]
resto = min[1]
seg = divmod(resto, 100)
seg_total = seg[0]
cen_total = seg[1]
# Imprimimos
print(f'El tiempo total de la carrera fue de {min_total}min : {seg_total}seg : {cen_total} centesimas')