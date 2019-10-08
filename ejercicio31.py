#ejercicio31
#Develop a program that reads a four-digit integer from the user and displays the sum
#of the digits in the number. For example, if the user enters 3141 then your program
#should display 3+1+4+1=9.
n= int(input('ingresa numero a sumar \n'))
n1= n //1000
n2=(n - n1*1000)//100
n3= (n - n1*1000 - n2*100)//10
n4= (n- n1*1000 - n2*100 - n3*10)
operacion= n1+n2+n3+n4
print('la suma de tu numero es', operacion)