##############################################
##########   INDICES REPETIDOS  ##############
##############################################

lista = [74, 53, 32, 39, 92, 8, 6, 97, 49, 75, 85, 66, 27, 25, 1, 23, 4, 17, 81, 8, 5, 24];
lista_indice = [];

for i in range(len(lista)):
    num1 = lista[i];
    for j in range(i+1,len(lista)):
        num2 = lista[j];
        if(num1 == num2):
            lista_indice.append(i);
            lista_indice.append(j);

print("\nLista = ", lista);
print("\nDada la lista, las posiciones que se repiten son: ",set(lista_indice));