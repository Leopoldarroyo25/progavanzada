#Positions on a chess board are identified by a letter and a number. The letter identifies
#the column, while the number identifies the row, as shown below:
#Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
#arithmetic to report the color of the square in that row. For example, if the user enters
#a1 then your program should report that the square is black. If the user enters d5
#then your program should report that the square is white. Your program may assume
#that a valid position will always be entered. It does not need to perform any error
#checking.
cor=input('Ingrese cordenada que desea')
if cor == '1a' or cor =='1c' or \
   cor == '1e' or cor == '1g' or \
   cor == '2b' or cor =='2d' or \
   cor == '2f' or cor == '2h' or \
   cor == '3a' or cor =='3c' or \
   cor == '3e' or cor == '3g' or \
   cor == '4b' or cor =='4d' or \
   cor == '4f' or cor == '4h'or \
   cor == '5a' or cor=='5c' or \
   cor == '5e' or cor== '5g' or \
   cor == '6b' or cor=='6d' or \
   cor == '6f' or cor== '6h' or \
   cor == '7a' or cor=='7c' or \
   cor == '7e' or cor== '7g'or \
   cor == '8b' or cor=='8d' or \
   cor == '8f' or cor== "8h":
       
   print('Es color negro')
else:
   cor == '1b' or cor=='1d'or \
   cor == '1b' or cor=='1d'or \
   cor == '1f' or cor== '1h'or \
   cor == '2a' or cor=='2c' or \
   cor == '2e' or cor== '2g' or \
   cor == '3b' or cor=='3d' or \
   cor == '3f' or cor== '3h' or \
   cor == '4a' or cor=='4c' or \
   cor == '4e' or cor== '4g' or \
   cor == '5b' or cor=='5d' or \
   cor == '5f' or cor== '5h' or \
   cor == '6a' or cor=='6c' or \
   cor == '6e' or cor== '6g'or\
   cor == '7b' or cor=='7d' or \
   cor == '7f' or cor== '7h'or \
   cor == '8a' or cor=='8c' or \
   cor == '8e' or cor== "8g" 
       
   print('color blanco')       
       