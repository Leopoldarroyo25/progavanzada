#ejercicio33
#A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
#percent. Write a program that begins by reading the number of loaves of day old
#bread being purchased from the user. Then your program should display the regular
#price for the bread, the discount because it is a day old, and the total price. All of the
#values should be displayed using two decimal places, and the decimal points in all
#of the numbers should be aligned when reasonable values are entered by the user.
p=int(input('ingrese cantidad de panes '))
desc=.60
pres=3.49
operacion1=(p *pres)
operacion2=operacion1*.60
operacion3=(operacion1-operacion2)
print('precio del pan sin descuento ' "%.2f" % operacion1, '|', 'decuento ' "%.2f" % operacion2, '|', 'precio total con descuneto ' "%.2f" % operacion3)