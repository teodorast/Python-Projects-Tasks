first_number = int(input())
second_number = int(input())
magic_number = int(input())
sequence_combination_counter = 0

combination_found = False

for i in range(first_number,second_number+1):
    for y in range(first_number, second_number+1):
        sequence_combination_counter+=1
        if i+y==magic_number:
            combination_found = True
            break
    if i+y==magic_number:
        combination_found = True
        break
      

if combination_found:
    print(f"Combination N:{sequence_combination_counter} ({i} + {y} = {magic_number})")
else:
    print(f"{sequence_combination_counter} combinations - neither equals {magic_number}")