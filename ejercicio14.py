##############################################
########## PRINCIPIO DE AJEDREZ ##############
##############################################

tablero = [['  ','  ','PB'], ['  ','PN','  '], ['  ','  ','  '], ['AN','  ','  ']];

print("\tPARTIDA DE AJEDREZ: ");
for i in range(4):
    print("\t\t\t----------------");
    for j in range(3):
        if(j == 0):
            print("\t\t\t| "+str(tablero[i][j])+" |", end = '');
        else:
            print(" "+str(tablero[i][j])+" |", end = '');
    print("");
    if(i == 3):
        print("\t\t\t----------------");

print("\t- PN: Peón negro\n\t- AN: Alfil negro\n\t- PB: Peón blanco.");

print("\n\tEs su turno: (Juega las piezas negras)");
print("");
piezaMover = input("\t- Que desea mover (Peon / Alfil): ").casefold();
while((piezaMover in ['peon','alfil']) == False):
    print("\tADVERTENCIA: Pieza invalida\n\tIntentalo de nuevo...");
    piezaMover = input("\t- Que desea mover (Peon / Alfil): ").casefold();

print("\t- A donde: ");
fila = int(input("\t   ~ Fila: "));
columna = int(input("\t   ~ Columna: "));
if(piezaMover == 'peon'):
    while(not ((fila == 0) and (columna == 1 or columna == 2))):
        print("\tADVERTENCIA: Movimiento Invalido\n\tIntentalo de nuevo...");
        print("\t- A donde:");
        fila = int(input("\t   ~ Fila: "));
        columna = int(input("\t   ~ Columna: "));
    tablero[fila][columna] = 'PN';
    tablero[1][1] = '  ';
else:
    while(not ((fila == 1 and columna == 2) or (fila == 2 and columna == 1))):
        print("\tADVERTENCIA: Movimiento Invalido\n\tIntentalo de nuevo...");
        print("\t- A donde:");
        fila = int(input("\t   ~ Fila: "));
        columna = int(input("\t   ~ Columna: "));
    tablero[fila][columna] = 'AN';
    tablero[3][0] = '  ';

print("\t- Movimiento realizado con exito");
print("\n\t>>> TABLERO ACTUALIZADO: ");
for i in range(4):
    print("\t\t\t----------------");
    for j in range(3):
        if(j == 0):
            print("\t\t\t| "+str(tablero[i][j])+" |", end = '');
        else:
            print(" "+str(tablero[i][j])+" |", end = '');
    print("");
    if(i == 3):
        print("\t\t\t----------------");
