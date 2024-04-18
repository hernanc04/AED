#Pedimos al usuario que ingrese los datos
name = input("Ingrese un nombre: ")
surname = input("Ingrese un apellido: ")
dom = input("Ingrese un dominio: ")

#Uso la funcion lower para que la direccion de mail me quede en minuscula
name_lower = name.lower()
surname_lower = surname.lower()
dom_lower = dom.lower()

#Realizamos el proceso
if name[0] == surname[0]:
    print(name_lower + "."+surname_lower + "@" + dom_lower)
else:
    print(name_lower[0] + surname_lower + "@" + dom_lower)
