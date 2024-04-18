# Carga de datos
apellido = input("Ingrese el apellido del candidato: ")
nombre = input("Ingrese el nombre del candidato: ")
votos = int(input("Ingrese la cantidad de votos: "))

# Muestra de datos
print(f"El candidato {apellido[0]} . {nombre[0]}, obtuvo ({votos}) votos\n {'x' * votos}")