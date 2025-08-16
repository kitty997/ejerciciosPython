temp_ayer = float(input("Ingresa la temperatura de ayer:"))
temp_hoy = float(input("Ingresa la temperatura de hoy:"))

if temp_hoy > temp_ayer:
    print("Hoy esta más caluroso que ayer")
elif temp_hoy==temp_ayer:
    print("Hoy esta igual que ayer")
else:
    print("Ayer estuvo más caluroso")

