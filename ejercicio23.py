#ejercicio 23
#A polygon is regular if its sides are all the same length and the angles between all of
#the adjacent sides are equal. The area of a regular polygon can be computed using
#the following formula, where s is the length of a side and n is the number of sides:
#Write a program that reads s and n from the user and then displays the area of a
#regular polygon constructed from these values.
import math
n=int(input('ingrese numero de lados \n'))
s=int(input('ingrese apotema \n'))
area= (n * math.pow(s, 2))/ ( 4 * math.tan(math.pi/n))
print('el area de tu poligono es %.4f' % area)