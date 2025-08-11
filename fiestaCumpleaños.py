# Dinero que tiene Ana
dinero_base = 500
dinero_extra = 50
dinero_total = dinero_base + dinero_extra

# Costos
pastel = 180
globos = 6 * 25
refrescos = 4 * 30
dulces = 3 * 40
decoraciones = 50

costo_total = pastel + globos + refrescos + dulces + decoraciones

diferencia = dinero_total - costo_total

print(f"Ana no tiene suficiente dinero. Le faltan ${abs(diferencia)} pesos.")
