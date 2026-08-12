c_llam = int(input("Ingrese las llamadas realizadas: "))
tc = float(input("Ingrese el tiempo total de comunicación: "))
ps = 1.5
cc = 12
seg_a_cobrar = (tc*ps)/ 1
llam_a_cobrar = (c_llam*cc)/1
precio_final = (seg_a_cobrar + llam_a_cobrar)
print("El precio a cobrar es $",precio_final)