# Solicitamos el precio
preciounit = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad comprada: "))
metodopago = int(input("Ingresa metodo de pago\n1) Efectivo\n2)Tarjeta\n:"))

# Desarrollamos
preciofinal = preciounit * cantidad
print(f"'El precio final por la cantidad de {cantidad} productos es de {preciofinal}")

if metodopago == 1 and cantidad > 10:
    descuento = preciofinal - preciofinal * 0.15
    print(f"Al pagar en efectivo se le aplicó un descuento del 15% quedandole en {descuento} ")
else:
    descuento = preciofinal - preciofinal * 0.05
    print(f"Se le realizó un descuento de 5% quedandole en {descuento}")