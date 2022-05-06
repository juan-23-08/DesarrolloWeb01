##############################################
##########   ELIMINAR PALABRA   ##############
##############################################

oracion = input("\nIngrese una oracion: ");
palabra_eliminar = input("\nIngrese la palabra a eliminar: ");
bandera = False;

lista = oracion.split();

print("\nBuscando Palabra a Eliminar...");
for i in range(len(lista)):
    if(lista[i].casefold() == palabra_eliminar.casefold()):
        lista.pop(i);
        bandera = True;
        break;

if(bandera):
    print("Palabra encontrada!! Ahora la eliminaremos...");
    
    oracion = "";
    print("\n¡Actualizando Oracion...!");
    for i in range(len(lista)):
        oracion += lista[i] + " ";
    oracion = oracion.rstrip().lstrip(); #Elimina los espacios en blanco de la parte final, #Elimina los espacios en blanco de la parte inicial
    print("Oracion Actualizada: ", oracion);
else:
    print("ADVERTENCIA: Palabra no encontrada");