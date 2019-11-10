#ejercicio55
#Electromagnetic radiation can be classified into one of 7 categories according to its
#frequency, as shown in the table below:
#Write a program that reads the frequency of the radiation from the user and displays
#the appropriate name.
LG=int(input('ingrese frecuencia'))
if LG == 3*10**9:
    print ('ondas de radio')
elif LG > 3*10**10 or LG <=3*10**12 :
    print('Microondas')
elif LG == 3*10**13 or LG <= 4.3*10**14:
    print('Luz infraroja')
elif LG == 4.3*10**15 or LG <= 7.5*10**14:
    print('Luz vicible')
elif LG == 7.5*10**15 or LG <= 3*10**17:
    print('Luz ultravioleta')
elif LG == 3*10**18 or LG <= 3*10**19:
    print('Rayos X')
elif LG == 3*10**19:
    print('Rayos Gamma')