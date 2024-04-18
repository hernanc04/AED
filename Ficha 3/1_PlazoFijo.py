# Carga de datos
cant_dinero = float(input("Ingrese la cantidad de dinero depositada en plazo fijo: "))
#Constante
tasa_fija = 20
# Desarrollo de datos
# saldo_final = cant_dinero * (1 + 0.023) - tasa_fija => Otra forma
saldo_final = (cant_dinero  +  (cant_dinero * 0.023) ) - tasa_fija

# Muestra de datos
print(f"El saldo final que tendrá la cuenta sería de ${saldo_final}")
