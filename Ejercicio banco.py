#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jazla
#
# Created:     11/08/2026
# Copyright:   (c) jazla 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------
#c= capital  i= incremento 6%  m= meses gm= ganancia mensual
#mf= monto final
c = float(input("Ingrese el capital a invertir: "))
m = float(input("Ingrese los meses a invertir: "))
i = 0.06
gm = (c*i)* m
mf = gm + c
print("Si usted invierte: ",c, "por: ",m,"meses, el monto final que obtendrá será de: ",mf)
