#ejercicio33
#A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
#percent. Write a program that begins by reading the number of loaves of day old
#bread being purchased from the user. Then your program should display the regular
#price for the bread, the discount because it is a day old, and the total price. All of the
#values should be displayed using two decimal places, and the decimal points in all
#of the numbers should be aligned when reasonable values are entered by the user.
a=int(input('ingrese numero'))
b=int(input('ingrese segundo numero'))
c=int(input('ingrese tercer numero'))
mn=min(a, b, c)
mx=max(a, b, c)
md=a + b + c - mn - mx 
print('los numeros ordenados son:')
print('', mn)
print('', md)
print('', mx)
