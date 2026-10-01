pronostico=float(input("Ingrese la probabilidad de que llueva"))
chicos=int(input("Indique cuantos chicos confirmaron que vienen"))
costoHamburgesas=5      #cada chico come 3
costoPancho=2       #cada chico come 4
peloteroGrande=500
peloteroChico=300
dinero=1000

cant_H = chicos*3
cant_P = chicos*4
precio_H = cant_H*costoHamburgesas
precio_P = cant_P*costoPancho
op1 = precio_H + peloteroGrande
op2 = precio_H + peloteroChico
op3 = precio_P + peloteroGrande
op4 = precio_P + peloteroChico

if pronostico > 65:
    if dinero >= op2:
      sobra = dinero - op2
      print("La fiesta es adentro con pelotero chico, la comida es hamburguesa, te va a sobrar:$ ", sobra)
    else:
      sobra = dinero - op4
      print("La fiesta es adentro con pelotero chico, la comida es pancho, te va a sobrar:$ ", sobra)

else:
    print("La fiesta es en el patio")
    if dinero >= op1:
        sobra = dinero - op1
        print("Reserva pelotero grande y la comida es hamburguesa, te va a sobrar:$ ", sobra)
    elif dinero >= op3:
        sobra = dinero - op3
        print("Reserva pelotero grande y la comida es pancho, te va a sobrar:$ ", sobra)
    elif dinero >= op2:
        sobra = dinero - op2
        print("Reserva pelotero chico y la comida es hamburguesa, te va a sobrar:$ ", sobra)
    else:
        if dinero >= op4:
         sobra = dinero - op4
         print("Reserva pelotero chico y la comida es pancho, te va a sobrar:$ ", sobra)
