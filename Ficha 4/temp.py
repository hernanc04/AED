#Pedimos las temperaturas
t1 = float(input("Ingrese la temperatura 1: "))
t2 = float(input("Ingrese la temperatura 2: "))
t3 = float(input("Ingrese la temperatura 3: "))

#Calculamos promedio
promedio = (t1 + t2 + t3) / 3

#Verificamos si existe una temperatura mayor al promedio y la mostramos
if (t1 or t2 or t3) > promedio:
    print("Existe una temperatura mayor al promedio.")