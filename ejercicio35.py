#Ejercicio 35
#It is commonly said that one human year is equivalent to 7 dog years. However this
#simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two
#human years as 10.5 dog years, and then count each additional human year as 4 dog
#years.

a=int(input('introduce años de perro '))
if a <= 2 :
    b= ('su ano', a*10.5)
else:
    b= 21 + (a - 1)*4
    print(b)