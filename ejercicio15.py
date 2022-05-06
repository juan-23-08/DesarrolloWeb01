##############################################
######### SUBCONJUNTOS NO VACIOS #############
##############################################

def subconjunto(lista, num):
    if(num == 1):
        for i in lista:
            print(f"\t{i}");
        num += 1;
        subconjunto(lista, num);
    elif(num == 2):
        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                print(f"\t{lista[i]} {lista[j]}")
        num += 1;
        subconjunto(lista, num);
    else:
        for i in lista:
            if(i==1):
                print(f"\t{i}", end=' ');
            else:
                print(f"{i}", end = ' ');

def subconjuntosNoVacios(numero):
    lista = [];
    for i in range(1,numero+1):
        lista.append(i);
    subconjunto(lista, 1);



subconjuntosNoVacios(3);