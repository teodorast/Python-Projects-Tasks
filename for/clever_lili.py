years = int(input())
washing_machine = float(input())
toy_price= int(input())
money_gifts = 0
toy_money = 0
stolen_money=0

for i in range(1,years + 1):
    if i % 2 == 0:
        money_gifts = money_gifts + (i*5)
        stolen_money=stolen_money + 1
    else:
        toy_money = toy_money + toy_price
    
total_money = money_gifts + toy_money - stolen_money

if total_money>=washing_machine:
    print(f"Yes! {(total_money-washing_machine):.2f}")

else:
    print(f"No! {abs(total_money-washing_machine):.2f}")
