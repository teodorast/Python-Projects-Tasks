command = input()
min_number = 98765432

while command!="Stop":
    is_number=int(command)
    if min_number>is_number:
        min_number=is_number

    command = input()
print(min_number)