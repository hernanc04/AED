# Carga de datos
dinero = input("Ingrese una cantidad de dinero expresado en numero con coma flotante:")

# dinero = float(input("Ingrese una cantidad de dinero (expresado en numero con coma flotante:"))
#signo = "$" + str(dinero) LA FUNCION str() SIRVE PARA TRANSFORMAR, CUALQUIER TIPO DE DATO A STRING
#pesos = "pesos " + (dinero)

# Procesos
signo = "$" + dinero
pesos = "pesos " + dinero

# Muestra en pantalla
print(f'Formato 1: Usted tiene {signo}')
print(f'Formato 2: Usted tiene {pesos}')