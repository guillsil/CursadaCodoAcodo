# Parametro por defecto

def calcularinteres(monto,plazo=12,TNA=12):
    print ('Total :',(monto+monto*TNA/12*plazo))

calcularinteres(5000)
calcularinteres(5000,24)
calcularinteres(500,18,15)










