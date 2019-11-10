#ejercicio54
#The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
#spectrum is continuous, it is often divided into 6 colors as shown below:
#Write a program thatreads a wavelengthfrom the user andreports its color. Display
#an appropriate error message if the wavelength entered by the user is outside of the
#visible spectrum
LG=int(input('ingrese longitud de onda'))
if LG == 380 or LG <= 449:
    print ('Violeta')
elif LG ==450 or LG <= 494:
    print('Azul')
elif LG == 495 or LG <= 569:
    print('Verde')
elif LG == 570 or LG <= 589:
    print('Amarillo')
elif LG == 590 or LG <= 620:
    print('Anaranjado')
elif LG == 620 or LG <= 750:
    print('red')
