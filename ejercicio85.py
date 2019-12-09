#ejercicio85
#Words like first, second and third are referred to as ordinal numbers. In this exercise,
#you will write a function that takes an integer as its only parameter and returns a
#string containing the appropriate English ordinal number as its only result. Your
#function must handle the integers between 1 and 12 (inclusive). It should return an
#empty string if a value outside of this range is provided as a parameter. Include a
#main program that demonstrates your function by displaying each integer from 1 to
#12 and its ordinal number. Your main program should only run when your file has
#not been imported into another program.

def o(numb):
    if numb < 20: #determining suffix for < 20
        if numb == 1: 
            suffix = 'st'
        elif numb == 2:
            suffix = 'nd'
        elif numb == 3:
            suffix = 'rd'
        else:
            suffix = 'th'  
    else:   #determining suffix for > 20
        tens = str(numb)
        tens = tens[-2]
        unit = str(numb)
        unit = unit[-1]
        if tens == "1":
           suffix = "th"
        else:
            if unit == "1": 
                suffix = 'st'
            elif unit == "2":
                suffix = 'nd'
            elif unit == "3":
                suffix = 'rd'
            else:
                suffix = 'th'
    return str(numb)+ suffix
    print(numb)