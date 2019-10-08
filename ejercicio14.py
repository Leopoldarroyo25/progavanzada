#ejercicio14
#Many people think about their height in feet and inches, even in some countries that
#primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program
#should compute and display the equivalent number of centimeters.
#pies=float(input('inserte el total de pies:'))
#pulgadas=float(input('inserte el total de pulgadas:'))

ft=pies*12
IN=ft+pulgadas

cm=IN*2.54

print('total de pulgadas',IN)
print('la equivalencia es:',cm,'cm')