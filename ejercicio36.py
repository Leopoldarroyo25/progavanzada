#ejercicio36
#In this exercise you will create a program that reads a letter of the alphabet from the
#user. If the user enters a, e, i, o or u then your program should display a message
#indicating that the entered letter is a vowel. If the user enters y then your program
#should display a message indicating that sometimes y is a vowel, and sometimes y is
#a consonant. Otherwise your program should display a message indicating that the
#letter is a consonant.
l=input('ingrese algunda letra')
if l== 'a' or l== 'e' or \
   l== 'i' or l== 'o' or \
   l== 'u':
   print('su leta es una vocal')
else:
    print('La letra es una consonante')