payment = input()
total_sum = 0

while payment!="NoMoreMoney":
    current_sum = float(payment)

    if current_sum<0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    
    total_sum+=current_sum

    payment = input()

print(f"Total: {total_sum:.2f}")   