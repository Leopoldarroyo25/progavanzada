#(Ejercicio 6: Hacer un programa en el que el usuario introdusca el nombre de la comida que ordeno en un restaurante y su precio. Despues su programa debe calcular el subtotal, el iva y la propina de toda la cuenta. La salida del programa debe parecerce a un ticket de restaurante. Use un IVA del 16% y una propina del 15% del subtotal. Los valores numericos deben de tener dos decimales.)
IVA=.16
propina=.15
nombreC1=input('Que comida ordenaste?')
precioC1=int(input('Precio de la comida ordenada?'))
nombreC2=input('Que comida ordenaste?')
precioC2=int(input('Precio de la comida ordenada?'))
nombreC3=input('Que comida ordenaste?')
precioC3=int(input('Precio de la comida ordenada?'))
nombreC4=input('Que comida ordenaste?')
precioC4=int(input('Precio de la comida ordenada?'))
nombreC5=input('Que comida ordenaste?')
precioC5=int(input('Precio de la comida ordenada?'))
Subtotal= (precioC1+precioC2+precioC3+precioC4 +precioC5)
iva= (precioC1 +precioC2 +precioC3 +precioC4 +precioC5) * IVA
print("Subtotal $%.2f." % Subtotal)
propina=Subtotal * propina
print ("IVA $%.2f." %iva)
print ("Propina $%.2f." % propina)
total=(Subtotal + iva + propina)
print('---------------------')
print ("Tu total es $%.2f." % total)



