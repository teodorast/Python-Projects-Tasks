figure = input()
area = 0 
import math
if figure =='square':
   a = float(input())
   area = a*a
   
elif figure == 'rectangle':
    a = float (input())
    b = float (input())
    area = a * b
  
elif figure == 'circle':
    a = float (input())
    area = a*a*math.pi 
    
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = (a*b)/2
else:
    print('Wrong Data!')
print(f'{area:.3f}')

