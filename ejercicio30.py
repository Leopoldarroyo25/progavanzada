#ejercicio30
# In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.
k=float(input('ingrese kilopascales \n'))
mi = k * (760 / 101.325)
at = k * (1/ 101.3)
print('en mmHg tu resultado es', mi)
print('tu resultado en atm es ', at)