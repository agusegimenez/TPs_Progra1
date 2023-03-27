# TP 1
"""
# Ejercicio 3
# funciones
def totalGastado(viajes, tarifa):
    if viajes <= 20:
        tarifaTotal = tarifa*viajes
    elif viajes <= 30:
        tarifaTotal = tarifa*viajes - ((tarifa*viajes)*0.2)
    elif viajes <= 40:
        tarifaToal = tarifa*viajes - ((tarifa*viajes)*0.3)
    else:
        tarifaTotal = tarifa*viajes - ((tarifa*viajes)*0.4)
    return tarifaTotal

# main
tarifaBasica = 250
viajes = int(input("Cuantos viajes hizo en el mes? "))
tarifaTotal = totalGastado(viajes,tarifaBasica)
print("El total gastado en viajes fue de", tarifaTotal, "$")

"""

# Ejercicio 4
# funciones
total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

if dinero_recibido < total_compra:
    print("Error: El dinero recibido es insuficiente.")
else:
    vuelto = dinero_recibido - total_compra
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    cantidad_billetes = []

    for i in range(len(denominaciones)):
        cantidad = vuelto // denominaciones[i]
        vuelto = vuelto % denominaciones[i]
        cantidad_billetes.append(cantidad)

    print("Cantidad de billetes a entregar:")
    for i in range(len(denominaciones)):
        if cantidad_billetes[i] > 0:
            print("$" + str(denominaciones[i]) + ": " + str(cantidad_billetes[i]))