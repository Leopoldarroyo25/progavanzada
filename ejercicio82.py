#ejercicio82
#En la Ciudad de Mexico la tarifa de taxi uber conciste en un precio base de $44 mas $12 por cada km recorrido. 
#Escriba una funcion que tome la distancia viajada(en km) el cual debe de ser el unico argumento y regrese la tarifa total #como resultado, escriba un programa que demuestre la funcion 
def tarifa(distancia):
    total= 44.00 + distancia*12.00
    return total
dist=float(input('insterte la distancia manejada(KM):  '))
cuota=tarifa(dist)
print(cuota)