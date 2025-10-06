# ==========================
# JUEGO DE AJEDREZ - MOVIMIENTO DE PEONES (AMBOS COLORES)
# ==========================

tablero = [['' for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        tablero[i][j] = 0

tablero[0] = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(1, 9):
    tablero[i][0] = str(9 - i)

# Piezas negras
tablero[1][1:] = [2, 3, 4, 5, 6, 4, 3, 2]
tablero[2][1:] = [1, 1, 1, 1, 1, 1, 1, 1]
# Piezas blancas
tablero[7][1:] = [1, 1, 1, 1, 1, 1, 1, 1]
tablero[8][1:] = [2, 3, 4, 5, 6, 4, 3, 2]


def mostrar_tablero(tab):
    print("\n  ===== TABLERO DE AJEDREZ =====")
    for fila in tab:
        print(" ".join(f"{str(x):^3}" for x in fila))
    print()


def coordenada_a_pos(coord):
    letras = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    if len(coord) != 2:
        return None
    col = letras.get(coord[0].lower(), None)
    if not coord[1].isdigit():
        return None
    fila = 9 - int(coord[1])
    if col is None or fila < 1 or fila > 8:
        return None
    return fila, col


# ==========================
# FUNCIÓN PARA MOVER PEONES (AHORA AMBOS COLORES)
# ==========================
def mover_peon(tab, fila_o, col_o):
    # Determinar color del peón
    if fila_o <= 2:  # peones negros
        nueva_fila = fila_o + 1
    elif fila_o >= 7:  # peones blancos
        nueva_fila = fila_o - 1
    else:
        # Si está en otra posición, asumimos que ya se ha movido antes:
        # el color depende de hacia dónde puede moverse
        # Blanco: si hay algo abajo, entonces se mueve hacia arriba
        if fila_o > 4:
            nueva_fila = fila_o - 1
        else:
            nueva_fila = fila_o + 1

    # Verificar que no salga del tablero
    if nueva_fila < 1 or nueva_fila > 8:
        print("❌ Movimiento inválido: el peón no puede salir del tablero.")
        return False

    # Verificar que la casilla esté vacía
    if tab[nueva_fila][col_o] != 0:
        print("❌ Movimiento inválido: hay una pieza bloqueando el camino.")
        return False

    # Realizar el movimiento
    tab[fila_o][col_o] = 0
    tab[nueva_fila][col_o] = 1
    print("✅ Movimiento realizado con éxito.")
    return True


def jugar(tab):
    mostrar_tablero(tab)
    print("Los números representan:")
    print("1 = Peón\n2 = Torre\n3 = Caballo\n4 = Alfil\n5 = Reina\n6 = Rey")
    print("\nEscriba 'off' para salir del juego.\n")

    while True:
        origen = input("Ingrese la coordenada de la ficha a mover (ejemplo a7): ").strip().lower()

        if origen == "off":
            print("\n🛑 Juego finalizado. ¡Gracias por jugar!")
            break

        pos = coordenada_a_pos(origen)
        if not pos:
            print("⚠️ Coordenada inválida. Intente nuevamente.\n")
            continue

        fila_o, col_o = pos
        ficha = tab[fila_o][col_o]

        if ficha == 0:
            print("⚠️ No hay ninguna ficha en esa posición.\n")
            continue
        elif ficha == 1:
            exito = mover_peon(tab, fila_o, col_o)
            if exito:
                mostrar_tablero(tab)
        else:
            print("⚠️ Movimiento de ficha no programado.\n")
            continue


# ==========================
# INICIO DEL PROGRAMA
# ==========================
jugar(tablero)
