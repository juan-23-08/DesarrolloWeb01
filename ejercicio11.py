##############################################
##########  SUSTITUIR PALABRA   ##############
##############################################

oracion = input("\nIngrese una oracion: ");
palabra_buscar = input("\nIngrese la palabra a buscar: ");
palabra_sustituta = input("Ingrese la palabra sustituta: ");
bandera = False;

lista = oracion.split();

print("\nBuscando Palabra...");
for i in range(len(lista)):
    if(lista[i].casefold() == palabra_buscar.casefold()):
        lista[i] = palabra_sustituta;
        bandera = True;
        break;

if(bandera):
    print("Palabra encontrada!! Ahora la sustituiremos...");
    
    oracion = "";
    print("\n¡Actualizando Oracion...!");
    for i in range(len(lista)):
        if(i == len(lista)-1):
            oracion += lista[i];
        else:
            oracion += lista[i] + " ";
    
    print("Oracion Actualizada: ", oracion);
else:
    print("ADVERTENCIA: Palabra no encontrada");