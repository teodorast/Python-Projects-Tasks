holiday = float(input())
number_puzzels = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_kamion = int(input())

income = number_puzzels * 2.6 + number_dolls * 3 + number_bears*4.10 + number_minions*8.2 + number_kamion*2

if number_puzzels + number_dolls + number_bears + number_minions + number_kamion >= 50:
    income = income - (income*0.25)
else: 
    income = number_puzzels * 2.6 + number_dolls * 3 + number_bears*4.10 + number_minions*8.2 + number_kamion*2

rent = income*0.10

final_income= income - rent - holiday

if final_income >= 0:
    print(f"Yes! {final_income:.2f} lv left.")
elif final_income<0:
    print(f"Not enough money! {abs(final_income):.2f} lv needed.")