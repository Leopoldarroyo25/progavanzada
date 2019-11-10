#ejercicio49
#The following table contains earthquake magnitude ranges on the Richter scale and
#their descriptors:
#Write a program that reads a magnitude from the user and displays the appropriate
#descriptor as part of a meaningful message. For example, if the user enters 5.5 then
#your program should indicate that a magnitude 5.5 earthquake is considered to be a
#moderate earthquake
escala=float(input('Ingrese su escala ritcher'))
if escala <= 2.0:
    print('Micro')
elif (escala >= 2.0 and escala <= 3.0):
    print('Very minor')
elif (escala >= 3.0 and escala <= 4.0):
    print('Minor')
elif (escala >= 4.0 and escala <= 5.0):
    print('Ligth')
elif (escala >= 5.0 and escala <= 6.0):
    print('Moderate')
elif (escala >= 6.0 and escala <= 7.0):
    print('Stronge')
elif (escala >= 7.0 and escala <= 8.0):
    print('Major')
elif (escala >= 8.0 and escala <= 10.0):
    print('Great')
elif (escala >= 10.0):
    print('Meteoric')
#print('tu escala es ', nivel)