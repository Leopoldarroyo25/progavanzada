#(In many juridiction a small deposit is added to drink containers to encourage people to recicle them. In one particular juridiction, drink containers holdin one liter or ledd have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.)
print('Welcome strange \n Introduzca botella \n e indique que tamano es su botella')
lmenos=.10
lomas=.25
menos=int(input('cuantas botellas chicas has ingresado?'))
mas=int(input('cuantas botellas grandes has ingresado?'))
operacion=menos * lmenos + mas * lomas
print("tu total es $%.2f." % operacion)