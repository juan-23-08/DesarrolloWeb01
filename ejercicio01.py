#############################################
#### PROGRAMA PARA CALCULAR EL MCM Y MCD ####
############# DE TRES NUMEROS ###############
intento = 0;
while intento < 2:
    mcm = 1;
    mcd = 1;
    listaMCM = [0, 0, 0];
    listaMCD = [0, 0, 0];

    for i in range(3):
        listaMCM[i] = int(input(f"Ingrese el numero {i+1}: "));
        listaMCD[i] = listaMCM[i];
        while(listaMCM[i] < 0):
            print("El numero debe de ser entero y positivo");
            listaMCM[i] = int(input(f"Ingrese el numero {i+1}: "));
            listaMCD[i] = listaMCM[i];

    print(listaMCM);

    for i in range(2,max(listaMCM)+1):
        a = listaMCM[0] % i;
        b = listaMCM[1] % i;
        c = listaMCM[2] % i;

        while(a == 0 or b == 0 or c == 0):
            if(a == 0):
                listaMCM[0] = listaMCM[0] // i;
            if(b == 0):
                listaMCM[1] = listaMCM[1] // i;
            if(c == 0):
                listaMCM[2] = listaMCM[2] // i;
            
            mcm = mcm * i;

            a = listaMCM[0] % i;
            b = listaMCM[1] % i;
            c = listaMCM[2] % i;

        if(listaMCM[0] == 1 and listaMCM[1] == 1 and listaMCM[2] == 1):
            break;

    print(f"MCM: {mcm}");

    print("\n");
    print(listaMCD);

    i = 2;
    while (i <= max(listaMCD)):
        a = listaMCD[0] % i;
        b = listaMCD[1] % i;
        c = listaMCD[2] % i;

        while(a == 0 and b == 0 and c == 0):
            listaMCD[0] //= i;
            listaMCD[1] //= i; 
            listaMCD[2] //= i;  
            
            mcd = mcd * i;

            a = listaMCD[0] % i;
            b = listaMCD[1] % i;
            c = listaMCD[2] % i;
            
        if(listaMCD[0] == 1 or listaMCD[1] == 1 or listaMCD[2] == 1):
            break;
        i += 1;

    print(f"MCD: {mcd}");
    intento += 1;