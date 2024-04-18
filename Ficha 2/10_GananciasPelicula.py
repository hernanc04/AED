# Carga de datos
total_recaudado = float(input("Ingrese el total que recaudó la pelicula: "))
participante = input("Ingrese el nombre del participante de la pelicula a abonar: ")
porc = float(input("Ingrese el porcentaje a pagar: "))

#Desarrollo
porc_a_pagar = total_recaudado * (porc / 100)

# Mostramos en pantalla
print(f"{participante} recibirá el monto de ${porc_a_pagar}")
