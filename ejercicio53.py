#ejercicio53
#At a particular company, employees are rated at the end of each year. The rating scale
#begins at 0.0, with higher values indicating better performance and resulting in larger
#raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
#between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
#with each rating is shown in the following table. The amount of an employee’s raise
#is $2400.00 multiplied by their rating.
#Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s
#raise should also be reported. Your program should display an appropriate error
#message if an invalid rating is entered.
aumento=2400.00
inaceptable=0
aceptable=0.4
meritorio=0.6
clasificacion=float(('ingrese clasificacion'))
if clasificacion== inaceptable:
    rendimiento='inaceptable'
elif clasificacion==aceptable:
    rendimiento='aceptable'
elif clasificacion >= meritorio:
    rendimiento='meritorio'
else:
    rendimiento =" "
if rendimiento=="":
    print('inserte rendimiento valido')
else:
    print('el rendimiento es %s.' % rendimiento)
    print('su aumento es de $%.2f.' %(rendimiento*aumento))