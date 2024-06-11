cp = input("Ingrese el código postal del lugar de destino: ") 
direccion = input("Dirección del lugar de destino: ") 
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): ")) 
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

es_argentina = len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[6:].isalpha() and cp[0].lower() != 'o' and cp[0].lower() != 'i'
es_bolivia = len (cp) == 4 and cp.isdigit()
es_brasil = len(cp) == 9 and cp[0:5].isdigit and cp[5] == '-' and cp[6:].isdigit()
es_chile = len(cp) == 7 and cp.isdigit()
es_paraguay = len(cp) == 6 and cp.isdigit()
es_uruguay = len(cp) == 5 and cp.isdigit()

# Comparo que pais es segun el codigo postal
if es_argentina:
    destino = 'Argentina'
    if cp[0].lower() == 'c':
        provincia = 'Ciudad Autónoma de Buenos Aires'
    elif cp[0].lower() == 'b':
        provincia = "Buenos Aires"
    elif cp[0].lower() == 'k':
        provincia = "Catamarca"
    elif cp[0].lower() == 'h':
        provincia = "Chaco"
    elif cp[0].lower() == 'h':
        provincia = "Chubut"
    elif cp[0].lower() == 'x':
        provincia = "Córdoba"
    elif cp[0].lower() == 'w':
        provincia = "Corrientes"
    elif cp[0].lower() == 'e':
        provincia = "Entre Ríos"
    elif cp[0].lower() == 'p':
        provincia = "Formosa"
    elif cp[0].lower() == 'y':
        provincia = "Jujuy"
    elif cp[0].lower() == 'l':
        provincia = "La Pampa"
    elif cp[0].lower() == 'f':
        provincia = "La Rioja"
    elif cp[0].lower() == 'm':
        provincia = "Mendoza"
    elif cp[0].lower() == 'n':
        provincia = "Misiones"
    elif cp[0].lower() == 'q':
        provincia = "Neuquén"
    elif cp[0].lower() == 'r':
        provincia = "Río Negro"
    elif cp[0].lower() == 'a':
        provincia = "Salta"
    elif cp[0].lower() == 'j':
        provincia = "San Juan"
    elif cp[0].lower() == 'd':
        provincia = "San Luis"
    elif cp[0].lower() == 'z':
        provincia = "Santa Cruz"
    elif cp[0].lower() == 's':
        provincia = "Santa Fe"
    elif cp[0].lower() == 'g':
        provincia = "Santiago del Estero" 
    elif cp[0].lower() == 'v':
        provincia = "Tierra del Fuego"
    elif cp[0].lower() == 't':
        provincia = "Tucumán"
elif es_bolivia:
    destino = "Bolivia"
    provincia = "No aplica"
elif es_brasil:
    destino = "Brasil"
    provincia = "No aplica"
elif es_chile:
    destino = "Chile"
    provincia = "No aplica"
elif es_paraguay:
    destino = "Paraguay"
    provincia = "No aplica"
elif es_uruguay:
    destino = "Uruguay"
    provincia = "No aplica"
else:
    destino = "Otro"
    provincia = "No aplica"
 
if destino == 'Argentina':
    if tipo == 0:
        inicial = 1100
        if pago == 1:
            final = int(1100 - (1100 * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = 1800
        if pago == 1:
            final = int(1800 - (1800 * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = 2450
        if pago == 1:
            final = int(2450 - (2450 * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = 8300
        if pago == 1:
            final = int(8300 - (8300 * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = 10900
        if pago == 1:
            final = int(10900 - (10900 * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = 14300
        if pago == 1:
            final = int(14300 - (14300 * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = 17900
        if pago == 1:
            final = int(17900 - (17900 * 0.1))
        else:
            final = inicial
elif destino == "Paraguay" or destino == "Bolivia" or (destino == "Uruguay" and int(cp[0]) == 1):
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = int(inicial)
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
elif destino == "Chile" or destino == "Uruguay":
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
elif destino == "Brasil" and (int(cp[0]) == 8 or int(cp[0]) == 9):
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.20))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
elif destino == "Brasil" and (int(cp[0]) == 0 or int(cp[0]) == 1 or int(cp[0]) == 2 or int(cp[0]) == 3 ):
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.25))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
elif destino == "Brasil" and (int(cp[0]) == 4 or int(cp[0]) == 5 or int(cp[0]) == 6 or int(cp[0]) == 7):
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.30))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
else:
    if tipo == 0:
        inicial = int(1100 + (1100 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 1:
        inicial = int(1800 + (1800 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 2:
        inicial = int(2450 + (2450 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 3:
        inicial = int(8300 + (8300 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 4:
        inicial = int(10900 + (10900 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 5:
        inicial = int(14300 + (14300 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    elif tipo == 6:
        inicial = int(17900 + (17900 * 0.50))
        if pago == 1:
            final = int(inicial - (inicial * 0.1))
        else:
            final = inicial
    
print("País de destino del envío:", destino) 
print("Provincia destino:", provincia) 
print("Importe inicial a pagar:", inicial) 
print("Importe final a pagar:", final)