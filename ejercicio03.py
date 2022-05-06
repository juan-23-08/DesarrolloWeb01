##############################################
###########   NUMEROS AMIGOS   ###############
##############################################

def lee_entero():
   while True:
       entrada = input("Escribe un numero entero: ");
       try:
           entrada = int(entrada);
           return entrada;
       except ValueError:
           print("La entrada es incorrecta: escribe un numero entero");

def suma_divisores(numero):
    suma = 0;
    if(numero <= 0):
        return suma;
    elif(numero <= 3):
        return 1;
    else:
        for i in range(1,(numero//2)+1):
            if(numero % i == 0):
                suma += i;
        return suma;

n = lee_entero();
sumDivN1 = -1;
sumDivN2 = -1;

for i in range(n):
    sumDivN1 = suma_divisores(i);
    if(sumDivN1 >= 3):
        sumDivN2 = suma_divisores(sumDivN1);
    if(i == sumDivN2):
        print(f"El numero {i} y {sumDivN1} son numeros amigos");
