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
