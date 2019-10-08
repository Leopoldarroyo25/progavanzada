#Ejercicio25
#(Crear un programa que le pida al usuario la duracion en dias, horas, minutos y segundos. Calcular y desplegar la cantidad totalde segundos de duracion.)
dias=int(input('Cuantos dias?'))
horas=int(input('cuntas horas?'))
minutos=int (input('cuantos minutos?'))
segundos=int (input('cuantos segundos?'))
d= dias*86400
h= horas*3600
m= minutos*60
s= 1*segundos


sumas= d + h + m + s
print(sumas)
