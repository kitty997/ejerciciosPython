stock = int(input("El número de manzanas:"))
pedido = int(input("Ingresa el número de manzanas:"))

if stock >= pedido:
    print("La venta se puede hacer")
else:
    print("No hay sufiente para la venta")