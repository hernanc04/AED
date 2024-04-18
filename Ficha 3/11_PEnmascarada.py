# Carga de datos
palabra = input("Ingrese una palabra: ")

# Procesos
pLetra = palabra[0]
uLetra = palabra[-1]
tamaño = len(palabra)

# Aca, concatenamos la primera letra con un asterisco que se multiplica por el tamaño de la cadena, restando 2 que serian las letras
transformacion = pLetra + "*" * (tamaño -3)  + uLetra

print(transformacion)