def abrirarchivo(nombre):
    archivo = open(nombre, 'r')
    return archivo


def destinoalfa(direccion):
    destino = direccion.split()
    altura = destino[-1].rstrip(".")
    
    if altura.isdigit():
        for palabra in destino[:-1]:
            if not palabra.isalnum():
                return False
        return True
    else:
        return False


def doblemayus(direccion):
    anterior = ''
    mayusdobles = False
    for car in direccion:
        if anterior.isupper() and car.isupper():
            mayusdobles = True
        anterior = car
    return mayusdobles


def main():
    archivo = abrirarchivo("envios25.txt")
    cl = 0
    control = ''
    esHC = esSC = False
    cedvalid = cedinvalid = 0
    
    
    #r1)
    line = archivo.readline()
    if 'HC' in line:
        control = "Hard Control"
        esHC = True
    elif 'SC' in line:
        control = "Soft Control"
        esSC = True
    else:
        esHC = esSC = False
    
    
    
    while True:
        line = archivo.readline()  # Leer la siguiente linea, ya se leyó la primera
        if not line:  # si no hay linea, terminar bucle
            break
        
        cp = line[0:9]
        direccion = line[9:29]
        tipo = line[29]
        pago = line[30]
        
        print(cp, direccion, tipo, pago)
        if ( esHC and destinoalfa(direccion) and not doblemayus(direccion) ) or esSC:
            cedvalid += 1
        else:
            cedinvalid += 1
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid) 
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)



main()
""" 

print(' (r4) - Total acumulado de importes finales:', imp_acu_total) 
print(' (r5) - Cantidad de cartas simples:', ccs) 
print(' (r6) - Cantidad de cartas certificadas:', ccc) 
print(' (r7) - Cantidad de cartas expresas:', cce) 
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor) 
print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp) 
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp) 
print('(r11) - Importe menor pagado por envios a Brasil:', menimp) 
print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp) 
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc) 
print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom) """