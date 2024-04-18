# Se solicita el dato
word = input("Ingrese una palabra: ")

# Calculamos la cantidad de letras
cantidad_letras = len(word)
print(f"La palabra {word} tiene {cantidad_letras} letras")

# Verificamos si el ultimo elemento es vocal
# el indice [-1] siempre hace referencia a la ultima posicion de la cadena
# if word[-1] == 'a'  or word[-1] == 'e' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u':
#     print("La palabra termina en una vocal.")
# else:
#     print("La palabra no termina en una vocal.")

#Otra manera de hacer
# con el operador in verificamos si el ultimo elemento de la cadena pertenece a la cadena 'aeiouAEIOU'
if word[-1] in "aeiouAEIOU":
    print("La palabra termina en una vocal.")
else:
    print("La palabra no termina en una vocal.")