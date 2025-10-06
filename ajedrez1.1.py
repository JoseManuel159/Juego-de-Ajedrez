tablero = [['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],
           ['','','','','','','','',''],]

for i in range(9):
    for j in range(9):
        tablero[i][j]=0




tablero[0] = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
tablero[1][1:] = [2, 3, 4, 5, 6, 4, 3, 2]
tablero[2][1:] = [1, 1, 1, 1, 1, 1, 1, 1]
tablero[7][1:] = [1, 1, 1, 1, 1, 1, 1, 1]
tablero[8][1:]= [2, 3, 4, 5, 6, 4, 3, 2] 

for i in range(1, 9):
    tablero[i][0] = str(9-i)


def mostrar_tablero(tab):
    for fila in tab:
        print(" ".join(f"{str(x):^3}" for x in fila))

mostrar_tablero(tablero)

print("\nLos números representan:")
print("1 = Peón, 2 = Torre, 3 = Caballo, 4 = Alfil, 5 = Reina, 6 = Rey")

#primer movimiento para los peones
origen = input("Ingrese la coordenada de la ficha a mover (ejemplo a7): ")
destino = int(input("Ingrese cuantos pasos dar 1 0 2: "))
match origen:
    case 'a7':
        tablero[2][1]=0
        if destino == 1:
            tablero[3][1]=1
        elif destino == 2:
            tablero[4][1]=1
        mostrar_tablero(tablero)
    case 'b7':
        tablero[2][2]=0
        if destino == 1:
            tablero[3][2]=1
        elif destino == 2:
            tablero[4][2]=1
        mostrar_tablero(tablero)
    case 'c7':
        tablero[2][3]=0
        if destino == 1:
            tablero[3][3]=1
        elif destino == 2:
            tablero[4][3]=1
        mostrar_tablero(tablero)
    case 'd7':
        tablero[2][4]=0
        if destino == 1:
            tablero[3][4]=1
        elif destino == 2:
            tablero[4][4]=1
        mostrar_tablero(tablero)
    case 'e7':
        tablero[2][5]=0
        if destino == 1:
            tablero[3][5]=1
        elif destino == 2:
            tablero[4][5]=1
        mostrar_tablero(tablero)
    case 'f7':
        tablero[2][6]=0
        if destino == 1:
            tablero[3][6]=1
        elif destino == 2:
            tablero[4][6]=1
        mostrar_tablero(tablero)
    case 'g7':
        tablero[2][7]=0
        if destino == 1:
            tablero[3][7]=1
        elif destino == 2:
            tablero[4][7]=1
        mostrar_tablero(tablero)
    case 'h7':
        tablero[2][8]=0
        if destino == 1:
            tablero[3][8]=1
        elif destino == 2:
            tablero[4][8]=1
        mostrar_tablero(tablero)
    case _:
        print('caso no balido')
