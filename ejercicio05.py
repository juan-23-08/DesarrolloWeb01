##############################################
##########   SUBIDA DEL DOLAR   ##############
##############################################

periodo = int(input("Ingrese el numero de dias a evaluar: "));
dicPrecioDolar = [];

for i in range(periodo):
    dia = i+1;
    precio = float(input(f"\nDIA: {dia}\nIngrese el precio del dolar: "));
    diccionario = {'dia': dia, 'precio': precio};
    dicPrecioDolar.append(diccionario);

print("\nPrecio del dolar = ",dicPrecioDolar);

precio_2 = dicPrecioDolar[periodo-1]['precio'];
precio_1 = dicPrecioDolar[periodo-2]['precio'];

alza = precio_2 - precio_1;
diaAlza = periodo - 1;

for i in range(periodo-1,0,-1):
    precio_2 = dicPrecioDolar[i]['precio'];
    precio_1 = dicPrecioDolar[i-1]['precio'];
    alza_actual = precio_2 - precio_1;
    if(alza < alza_actual):
        alza = alza_actual;
        diaAlza = i;

if(alza == 0):
    print("\nNo hubo una alza!!");
else:
    print("\nLa mayor alza fue de: S/. {r:1.2f} entre los dias {a} y {b}".format(r=alza, a=diaAlza, b=diaAlza+1));
