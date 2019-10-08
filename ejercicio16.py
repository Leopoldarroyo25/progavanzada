# ejercicio 16
#Write a program that begins by reading a radius, r, from the user. The program will
#continue by computing and displaying the area of a circle with radius r and the
#volume of a sphere with radius r. Use the pi constant in the math module in your
#calculations.
pi=3.1416
r=float(input('inserte el radio:'))


area=float((pi)*(r*r))

volumen=float((3/4)*(pi)*(r*r*r))

print('area del circulo:',area)
print('volumen de la esfera:', volumen)