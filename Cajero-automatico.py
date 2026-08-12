dinero = float(input("Ingrese la cantidad de dinero deseado: "))
dinero_solicitado = dinero
cociente1000 = dinero_solicitado // 1000
dinero_solicitado = dinero_solicitado % 1000
cociente500 = dinero_solicitado // 500
dinero_solicitado = dinero_solicitado % 500
cociente200 = dinero_solicitado // 200
dinero_solicitado = dinero_solicitado % 200
cociente100 = dinero_solicitado // 100
dinero_solicitado = dinero_solicitado % 100
cociente50 = dinero_solicitado // 50
dinero_solicitado = dinero_solicitado % 50
cociente10 = dinero_solicitado // 10
dinero_solicitado = dinero_solicitado % 10
print("Usted solicitó: $",dinero)
print("billetes de $1000: ",cociente1000)
print("billetes de $500: ",cociente500)
print("billetes de $200: ",cociente200)
print("billetes de $100: ",cociente100)