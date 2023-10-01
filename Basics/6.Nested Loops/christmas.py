user_command = input()
adults_count= 0
children_count = 0


while user_command!="Christmas":
    years = int(user_command)
    if years<=16:
        children_count+=1
    elif years>16:
        adults_count+=1
    
    user_command=input()


toys_money = children_count*5
sweater_money = adults_count*15

print(f"Number of adults: {adults_count}" )
print(f"Number of kids: {children_count}")
print(f"Money for toys: {toys_money}")
print(f"Money for sweaters: {sweater_money}")



