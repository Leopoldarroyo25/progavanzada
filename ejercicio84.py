#ejercicio84
#Write a function that takes three numbers as parameters, and returns the median value
#of those parameters as its result. Include a main program that reads three values from
#the user and displays their median.


def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if  b < a and a < c or b > a and a > c:
        return a
    if  c < a and b < c or c > a and b > a:
        return c
    
def alternateMedia(a , b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)
def main():
    
    x = float(input('ingrese el primer valor:  '))
    y = float(input('ingrese el segundo valor:  '))
    z = float(input('ingrese el tercer valor:   '))
    
    print(" el valor de la media es  ", median(x, y, z))
    print("Usando el metodo alternativo es: ", alternateMedia(x, y, z))
    
main()