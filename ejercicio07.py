##############################################
##########    PUNTO DE SILLA    ##############
##############################################

lista = [];

fila = int(input("Ingrese fila: "));
columna = int(input("Ingrese columna: "));

for i in range(fila):
    lista.append([0]*columna);
print("");

for i in range(fila):
    for j in range(columna):
        lista[i][j] = int(input(f"Ingrese elemento [{i}][{j}]: "));
print("");

bandera = False;
minimo_fila = min(lista[0]);
indiceFila = 0;
indiceColumna = lista[0].index(minimo_fila);
contador = 0;

for i in range(fila):
    minimo_fila = min(lista[i]);
    indiceFila = i;
    indiceColumna = lista[i].index(minimo_fila);
    for j in range(fila):
        if(minimo_fila >= lista[j][indiceColumna]):
            bandera = True;
            contador += 1;
        else:
            bandera = False;
            contador = 0;
            break;
    if(contador == fila):
        break;

for i in range(fila):
    for j in range(columna):
        print(lista[i][j], end = " ");
    print("");

if(bandera):
    print(f"\nEl punto de silla esta en la ubicacion: {indiceFila}, {indiceColumna}");