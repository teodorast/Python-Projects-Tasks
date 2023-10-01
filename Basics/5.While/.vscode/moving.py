size1 = int(input())
size2 = int(input())
size3 = int(input())
free_space= size1*size2*size3
sum_of_boxes = 0
user_command = input()
diff = 0


while user_command!="Done":
    number_of_boxes = int(user_command)
    sum_of_boxes+=number_of_boxes
    diff = free_space - sum_of_boxes
    if diff<0:
        break

    user_command = input()


if user_command=="Done" and diff >=0:
    print(f"{diff} Cubic meters left.")

else:
    print(f"No more free space! You need {abs(diff)} Cubic meters more.")


