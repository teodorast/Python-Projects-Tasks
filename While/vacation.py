needed_money = float(input())
available_money = float(input())

days_counter = 0
money_counter = 0 

spending_counter = 0


while True :
    user_command = input()
    spend_or_save = user_command
    sum_to_spend_or_save = float(input())

    days_counter+=1

    if spend_or_save == "save":
        available_money+=sum_to_spend_or_save
        spending_counter = 0

    elif spend_or_save =="spend":
        available_money -= sum_to_spend_or_save
        spending_counter+=1
        
        if available_money<=0:
                available_money = 0

    if available_money >= needed_money or spending_counter == 5:
        break

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")

