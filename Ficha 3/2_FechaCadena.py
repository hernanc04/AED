# Cargamos los datos
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")

#Desarrollo
dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]

# Muestra en pantalla
print(f"Dia: {dia}, Mes: {mes}, Año: {anio}")