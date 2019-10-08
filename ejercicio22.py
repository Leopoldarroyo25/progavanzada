#ejercicio22
#In the previous exercise you created a program that computed the area of a triangle
#when the length of its base and its height were known. It is also possible to compute
#the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
#be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
#can be calculated using the following formula:
#area = sqr s × (s − s1) × (s − s2) × (s − s3)
#Develop a program that reads the lengths of the sides of a triangle from the user and
#displays its area.
import math
s=int(input('increse longitud 1 \n'))
s1=int(input('ingrese longitud 2 \n'))
s2=int(input('ingrese longitud 3 \n'))
s3=int(input('ingrese longitud 4 \n'))
operacion= math.sqrt(s*(s-s1)*(s-s2)*(s-s3))/2
print('area = %.2f' % operacion)