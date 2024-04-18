# Datos
largo = int(input("Ingresa el largo en metros de la parcela: "))
ancho= int(input("Ingresa el ancho en metros de la parcela: "))

#Desarrollo
# Calculo el area en m2
area = largo * ancho

# Quintales (cada 10 m2 son 2 quintales)
quintales = (area * 2)  //  10

# Se muestra en pantalla
print(f'Se pueden producir {quintales} quintales de trigo. ')