##############################################
########### HACER UN HISTOGRAMA ##############
##############################################

def generaGraficoEstadistico(lisParam):
    print("");
    print(lisParam);
    print("");
    for i in range(len(lisParam)):
        print("*"*lisParam[i]);

n = int(input("Ingrese el numero de elementos de la lista: "));

lista = [];
print("");
for i in range(n):
    n1 = int(input(f"Ingrese el numero {i+1} de su lista: "));
    lista.append(n1);

generaGraficoEstadistico(lista);