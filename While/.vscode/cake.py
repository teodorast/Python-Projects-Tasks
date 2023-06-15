cake_size1 = int(input())
cake_size2 = int(input())
sum_pieces = 0
cake_diff=0
cake_pieces = cake_size1 * cake_size2

user_command = input()

while user_command!="STOP":
    wanted_pieces = int(user_command)

    sum_pieces+=wanted_pieces
    cake_diff=cake_pieces-sum_pieces
    if cake_diff<0:
        break

    user_command = input()



if user_command == "STOP" and cake_diff>0:
    print(f"{cake_diff} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_diff)} pieces more.")

