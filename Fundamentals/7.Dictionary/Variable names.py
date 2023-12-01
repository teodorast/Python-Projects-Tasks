import re
variable_names = []
while True:
    input_string = input()
    if not input_string:
        break

    matches = re.findall(r'\b_([A-Za-z0-9]+)\b', input_string)
    
    variable_names.extend(matches)

print(','.join(variable_names))
