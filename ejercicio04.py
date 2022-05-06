##############################################
###########   PLANTAR ARBOLES  ###############
##############################################

import random;

matriz = [];

fila = int(input("Ingrese el numero de filas: "));
columna = int(input("Ingrese el numero de columnas: "));

areaTotal = fila * columna;
areaPlantada = 0;

for i in range(fila):
    matriz.append([" "]*columna);

for i in range(fila):
    for j in range(columna):
        matriz[i][j] = random.choice(" *");
        if(matriz[i][j] == "*"):
            areaPlantada += 1;

print("");
for i in range(fila):
    for j in range(columna):
        if(j == 0):
            print("\t", (matriz[i][j]), end = '  ');
        else:
            print(matriz[i][j], end = '  ');
    print("");

print(f"Area Total    : {areaTotal} <> 100.0 %"
        +f"\nArea Plantada : {areaPlantada} <>  {areaPlantada*100/areaTotal} %"
        +f"\nArea Libre    : {areaTotal-areaPlantada} <>  {100 - (areaPlantada*100/areaTotal)} %");
