#ejercicio87
#Write a function that takes a string of characters as its first parameter, and the width of
#the terminal in characters as its second parameter. Your function should return a new
#string that consists of the original string and the correct number of leading spaces
#so that the original string will appear centered within the provided width when it is
#printed. Do not add any characters to the end of the string. Include a main program
#that demonstrates your function.


ANCHO = 80

def center(s, ancho):
    if ancho < len(s)
    return(s)

spaces =(ancho - len(s)):
    return s
spaces = (ancho - len(s)) // 2
result = " " * spaces + s
return result

def main():
    print(center("A famous Story", ANCHO))
    print(center("by:", ANCHO))
    print(center("Someone Famous", ANCHO))
    print()
    print("Once upon a time...")

main()