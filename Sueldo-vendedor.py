#basico= $42000 comision= 10%(0.1)
v1 = float(input("Ingrese la primer venta: "))
v2 = float(input("Ingrese la segunda venta: "))
v3 = float(input("Ingrese la tercer venta: "))
basico= 42000
comision= 0.1
sum_ventas= v1 + v2 + v3
sueldo_x_com= (sum_ventas*0.1)
sueldo= (basico + sueldo_x_com)
print("El sueldo final del vendedor será: $",sueldo)
