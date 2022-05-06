##############################################
##########   CREAR DOS LISTAS   ##############
######### Y ELIMINAR DE LA 2 LA 1 ############

lista1 = [];
lista2 = [];

n1 = int(input("Ingrese el tamaño de la lista 1: "));
n2 = int(input("Ingrese el tamaño de la lista 2: "));

print(f"\nLISTA 1: {lista1}");
print("---------------------------------------------------------------------------------");
for i in range(n1):
    elem = input(f"Ingrese el elemento {i+1}: ");
    lista1.append(elem);
print(f"\nLISTA 1: {lista1}");
print("_________________________________________________________________________________");

print(f"\nLISTA 2: {lista2}");
print("---------------------------------------------------------------------------------");
for i in range(n2):
    elem = input(f"Ingrese el elemento {i+1}: ");
    lista2.append(elem);
print(f"\nLISTA 2: {lista2}");
print("_________________________________________________________________________________");

print("\n..:: Eliminando elementos de la lista 2 a la lista 1 ::..");
for i in lista2:
    if(i in lista1):
        lista1.remove(i);

print(f"\nLista Actualizada: {lista1}");