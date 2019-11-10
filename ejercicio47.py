#ejercicio 47
#The horoscopes commonly reported in newspapers use the position of the sun at the
#time of one’s birth to try and predict the future. This system of astrology divides the
#year into twelve zodiac signs, as outline in the table below:

sig=(input('introduce tu mes de naciemineos \n'))
di= int(input('introduce dia de cumplenos \n'))
if sig == 'Diciembre' and di <= 22:
    print('Sagitario')
elif sig == 'Enero' and di > 19:
    print('Acuario')
elif sig == 'Febrero' and di < 19:
    print('Pscisis')
elif sig == 'Marzo' and di >= 21:
    print('Aries')
elif sig == 'Abril' and di >= 20:
    print('Pscisis')
elif sig == 'Mayo' and di <= 22:
    print('Tauro')
elif sig == 'Junio' and di <= 21:
    print('Geminis')
elif sig == 'Julio' and di >=23:
    print('Cancer')
elif sig == 'Agosto' and di <= 22:
    print('Leo')
elif sig == 'Septiembre' and di >= 23:
    print('Virgo')
elif sig == 'Octubre' and di >= 23:
    print('Libra')
elif sig == 'Noviembre' and di >= 22:
    print('Sagitario')
