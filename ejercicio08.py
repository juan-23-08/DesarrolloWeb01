##############################################
##########    SUMA DE CUBOS     ##############
##############################################

numeros = [];
suma_de_cubos = 0;

for i in range(150, 410):
    numero_letra = str(i);
    for i in numero_letra:
        suma_de_cubos += int(i)**3;
    if(suma_de_cubos == int(numero_letra)):
        numeros.append(int(numero_letra));
    suma_de_cubos = 0;

print(f"\nNumeros que pueden ser representados por la suma de los cubos de sus digitos:\n\t{numeros}");