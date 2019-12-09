#ejercicio90
#Many people do not use capital letters correctly, especially when typing on small
#devices like smart phones. In this exercise, you will write a function that capitalizes
#the appropriate characters in a string. A lowercase “i” should be replaced with an
#uppercase “I” if it is both preceded and followed by a space. The first character in
#the string should also be capitalized, as well as the first non-space character after a
#“.”, “!” or “?”. For example, if the function is provided with the string “what time
#do i have to be there? what’s the address?” then it should return the string “What
#time do I have to be there? What’s the address?”. Include a main program that reads
#a string from the user, capitalizes it using your function, and displays the result.

def isInteger(s):
    s=s.strip()
    
    if (s[0]== "+" or s[0]=="-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

def main():
    s=input("introduzca texto: ")
    if isInteger(s):
        print("Esa Texto represta un entero.")
    else:
        print("Este texto no e sun entero")
        
    if __name__ =="__main__":
        main()
    