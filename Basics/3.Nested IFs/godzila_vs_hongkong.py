budget = float(input())
statists = int(input())
clothing_price = float(input())

if statists >=150:
    decor = budget * 0.10
    clothing_expense = clothing_price * statists - (clothing_price * statists*0.10)
else:
    decor = budget * 0.10
    clothing_expense = clothing_price * statists


final_prices = budget - decor - clothing_expense

if final_prices <0:
    print("Not enough money!")
    print(f"Wingard needs {abs(final_prices):.2f} leva more.")
    

elif final_prices >= 0:
    print("Action!")
    print(f"Wingard starts filming with {final_prices:.2f} leva left.")
    