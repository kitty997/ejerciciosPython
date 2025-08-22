print("=" * 50)
print("Bienvenidos al juega piedra, papel o tijera")
print("=" * 50)
jugador_1 = (input("¿Qué eliges: piedra, papel o tijera? "))
jugador_2 = (input("¿Qué eliges: piedra, papel o tijera? "))

print("El jugador uno selecciono",jugador_1)
print("El jugador dos selecciono",jugador_2)

if jugador_1 == jugador_2:
    print("Empate: ambos eligieron lo mismo")
elif (jugador_1 == "piedra" and jugador_2 == "tijera") or(jugador_1 == "tijera" and jugador_2 == "papel") or(jugador_1 == "papel" and jugador_2 == "piedra"):
    print("el jugador uno es el ganador")
else:
    print("El jugador dos es el ganador ")



