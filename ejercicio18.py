#Ejercicio 18
#The volume of a cylinder can be computed by multiplying the area of its circular
#base by its height. Write a program that reads the radius of the cylinder, along with
#its height, from the user and computes its volume. Display the result rounded to one
#decimal place.

import math
altura=int(input("Ingrese la Alturadel cilindro:"))
radio=int(input("Ingrese el Radio del cilindro:"))   
volumen=math.pi*radio**2*altura 
print("El volumen del cilindro es:",(volumen))