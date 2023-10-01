user_command = input()

sum_prime=0
sum_non_prime=0

while not user_command =='stop':
    number = int(user_command)

    if number<0:
        print("Number is negative.")
        user_command=input()
        continue

    is_Prime=True

    for current_number in range(2,number):
        if number%current_number==0:
            is_Prime=False
            break

    
    if is_Prime==True:
        sum_prime+=number
    else:
        sum_non_prime+=number



    user_command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")