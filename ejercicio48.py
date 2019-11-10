#ejercicio48
#The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
#shown in the table below. The pattern repeats from there, with 2012 being another
#year of the dragon, and 1999 being another year of the hare.
#Write a program that reads a year from the user and displays the animal associated
#with that year. Your program should work correctly for any year greater than or equal
#to zero, not just the ones listed in the table.
ano=int(input('Ingrese ano'))
if ano % 12 == 8:
    animal = 'Dragon'
elif ano % 12 == 9:
    animal ='Serpiente'
elif ano % 12 == 10:
    animal ='caballo'
elif ano % 12 == 11:
    animal = 'oveja'    
elif ano % 12 == 0:
    animal = 'Mono'
elif ano % 12 == 1:
    animal = 'Gallo'    
elif ano % 12 == 2:
    animal = 'perro'    
elif ano % 12 == 3:
    animal = 'Cerdo'    
elif ano % 12 == 4:
    animal = 'Rata'
elif ano % 12 == 5:
    animal = 'Buey'  
elif ano % 12 == 6:
    animal ='Tigre'
elif ano % 12 == 7:
    animal ='Liebre'      
print("%d este es el ano de %s." % (ano, animal) )