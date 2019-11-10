#ejercicio46
#The year is divided into four seasons: spring, summer, fall and winter. While the
#exact dates that the seasons change vary a little bit from year to year because of the
#way that the calendar is constructed, we will use the following dates for this exercise:
#Spring March 20
#Summer June 21
#Fall September 22
#Winter December 21
M=input('ingrese Mes ')
D=int(input('Ingrese Dia '))
if M=='Enero' or M=='Febrero':
    estacion="Invierno"
elif M=='Marzo':
  if D <20:
    estacion="Invierno"
  else:
        estacion="Primavera"
elif M == 'Abril' or M=='Mayo':
  estacion = "Primavera"
elif M == 'Junio':
  if D <21:
      estacion== "Primavera"
  else:
          estacion== "Verano"
elif M=="Sempiembre":
    if D < 22:
        estacion="Verano"
    else:
        estacion= "Otono"
elif M == "Octubre" or M == "Noviembre":
    estacion="otono"
elif M== "Diciembre":
  if D < 21:
      estacion = "otono"
  else:
      estacion="Invierno"   
print(M, D, 'es', estacion)
    
    