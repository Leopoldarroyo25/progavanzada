#ejericicio51
#At a particular university, letter grades are mapped to grade points in the following
#manner:
#Write a program that begins by reading a letter grade from the user. Then your
#program should compute and display the equivalent number of grade points. Ensure
#that your program generates an appropriate error message if the user enters an invalid
#letter grade
A = 4.0
Amenos=3.7
Bmas=3.3
B=3.0
Bmenos=2.7
Cmas=2.3
C=2.0
Cmenos=1.3
Dmas=1.3
D=1.0
F=0
invalido=-1
letter = input("introdice grado de letra: ")
letter = letter.upper()
if letter=='A+' or letter == 'A':
    gp=A
elif letter == 'A-':
    gp=Amenos
elif letter == 'B+':
    gp=Bmas
elif letter == 'B':
    gp=B
elif letter == 'B-':
    gp=Bmenos
elif letter == 'C+':
    gp=Cmas
elif letter == 'C':
    gp=C
elif letter == 'C-':
    gp=Cmenos
elif letter == 'D+':
    gp=Dmas
elif letter == 'D':
    gp=D
elif letter == 'F':
    gp=F
else:
    gp=invalido
    
if gp==invalido:
   print('no es valido tu nuemro de puntos')
else:
    print("tienes", gp, " grado de puntos")
    