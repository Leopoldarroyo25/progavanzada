#ejercicio52
#In the previous exercise you created a program that converts a letter grade into the
#equivalent number of grade points. In this exercise you will create a program that
#reverses the process and converts from a grade point value entered by the user to a
#letter grade. Ensure that your program handles grade point values that fall between
#letter grades. These should be rounded to the closest letter grade. Your program
#should report A+ for a 4.0 (or greater) grade point average.
#4.0 = A 
#3.7 = Amenos
#3.3 = Bmas
#3.0 = B
#2.7 = Bmenos
#2.3 = Cmas
#2.0 = C
#1.7 = Cmenos
#1.3 = Dmas
#1.0 = D
#0 = F
#-1 = invalido
num=float(input('ingresa calificacion'))
if num >= 4.0:
    print('A+')
elif num <= 3.7 and num >= 3.4:
    print('A-')
elif num <=3.3 and num >=2.9:
    print('B+')
elif num <=3.0 and num >=2.6:
    print('B')
elif num <= 2.7 and num >=2.2:
    print('B-')
elif num <=2.3 and num >=1.9:
    print('C+')
elif num <=2.0 and num >= 1.6:
    print('C')
elif num <=1.7 and num >=1.2:
    print('C-')
elif num <=1.3 and num >=0.9:
    print('D+')
elif num <=1.0 and num == 0:
    print ('D')
else :
   print('no es valido tu nuemro de puntos')