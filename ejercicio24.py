#Create a program that reads a duration from the user as a number of days, hours,
#minutes, and seconds. Compute and display the total number of seconds represented
#by this duration.
h= int(input('ingrese horas \n'))
m= int(input('ingrese minutos \n'))
s= int(input('ingrese segundos \n'))
oh= h * 3600
om= m * 60
op= oh + om + s
print('los segundos totateles son ', op)