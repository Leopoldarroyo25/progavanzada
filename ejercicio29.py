#ejercicio29
#Write a program that begins by reading a temperature from the user in degrees
#Celsius. Then your program should display the equivalent temperature in degrees
#Fahrenheit and degrees Kelvin. The calculations needed to convert between different
#units of temperature can be found on the internet.
C=float(input('ingrese temperatura en grados celcius \n '))
F=(9/5 * C) + 32
print('Fahrenheit %.4f' % F)