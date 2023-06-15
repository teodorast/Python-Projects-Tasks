budget = float(input())
videocards_number = int(input())
processors_number = int(input())
ram_number = int(input())

final_price = videocards_number*250 + processors_number*(videocards_number*250*0.35) + ram_number*(videocards_number*250*0.10)

if videocards_number>processors_number:
    final_price = final_price - (final_price*0.15)
else:
    final_price=final_price

diff = budget - final_price

if diff>=0:
    print(f"You have {diff:.2f} leva left!")
elif diff < 0:
    print(f"Not enough money! You need {abs(diff):.2f} leva more!")