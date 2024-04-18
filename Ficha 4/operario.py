#Solicitamos el ingreso de datos
turno = int(input("Ingrese el turno que se trabajó \n1)- Diurno\n2)- Nocturno\n:"))
horas = int(input("Ingrese la cantidad de horas trabajadas: "))

#Desarrollamos el problema
if turno == 2:
    pago = horas * 40.60
elif turno == 1:
    pago = horas * 35.50

#Mostramos en que turno trabaja y cuanto cobrara de acuerdo a las horas que trabajó
print(f"Trabajas en el turno {turno} y por tus horas trabajadas cobrarás {pago}")