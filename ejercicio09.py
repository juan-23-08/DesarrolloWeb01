##############################################
##########   CONTAR PALABRAS    ##############
##############################################

def convertStrToList(cadena):
    agregar_palabra = "";
    listaPalabra = [];
    contador = 0;

    for i in cadena:
        contador += 1;
        if(i != " " and i != ","):
            agregar_palabra += i;
        else:
            if(agregar_palabra != ""):
                listaPalabra.append(agregar_palabra);
            
            agregar_palabra = "";
        if(len(cadena) == contador):
            listaPalabra.append(agregar_palabra);

    return listaPalabra;

def convertStrToDict(cadena):
    lista = convertStrToList(cadena);
    palabra = "";
    numVeces = 0;

    diccionario = {};

    for i in lista:
        palabra = i.lower();
        for j in range(len(lista)):
            aux = lista[j].lower();
            if(palabra == aux):
                numVeces += 1;
        if(not (palabra in diccionario)):
            diccionario[palabra] = numVeces;
        numVeces = 0;
    
    return diccionario;

cadena = input("Ingrese la cadena: ");
diccionarioCadena = convertStrToDict(cadena);

print(diccionarioCadena);