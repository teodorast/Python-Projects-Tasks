import re

numbers = []

while True:
    input_string = input()
    if not input_string:
        break

    
    extracted_numbers = re.findall(r'\d+', input_string)
    
   
    numbers.extend(extracted_numbers)


print(' '.join(numbers))