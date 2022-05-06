##############################################
##########   VALIDAR ENTRADAS   ##############
##############################################

alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z');
genero = ('masculino', 'femenino');

def nombreCorrecto(nombre):
    temp = 0;
    for i in nombre:
        if(i.casefold() in alfabeto):
            temp += 1;
    if(temp == len(nombre)):
        return True;
    else:
        return False;

def edadCorreca(edad):
    try:
        edad = int(edad);
        if(edad < 0 or edad > 120):
            return False;
        else:
            return True;
    except ValueError:
        return False;

def sexoCorrecto(sexo):
    if(sexo.casefold() in genero):
        return True;
    else:
        return False;

nombre = input("\nIngrese su nombre: ");

while(nombreCorrecto(nombre) == False):
    print("-------------------------------------------------");
    print("ADVERTENCIA: Ingrese solo caracteres del alfabeto");
    print("-------------------------------------------------");
    nombre = input("Ingrese su nombre: ");

edad = input("\nIngrese su edad: ");

while(edadCorreca(edad) == False):
    print("-------------------------------------------------------------------");
    print("ADVERTENCIA: La edad debe de ser un numero en un rango de [0 ; 120]");
    print("-------------------------------------------------------------------");
    edad = input("Ingrese su edad: ");
edad = int(edad);

sexo = input("\nIngrese su sexo (Masculino / Femenino): ");

while(sexoCorrecto(sexo) == False):
    print("--------------------------------------------------");
    print("ADVERTENCIA: Su sexo debe ser Masculino o Femenino");
    print("--------------------------------------------------");
    sexo = input("Ingrese su sexo (Masculino / Femenino): ");

print("\nNombre: ",nombre);
print("Edad: ",edad)
print("Sexo: ",sexo);
