adventure_days = int(input())
players_num = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())


current_food = food_per_day*players_num*adventure_days
current_water = water_per_day*players_num*adventure_days
current_energy = energy

day_for_water = 0
day_for_food = 0

for day in range(1,adventure_days+1):
    lost_energy = float(input())
    current_energy-=lost_energy

    day_for_water+=1
    if day_for_water>=2:
        current_water-=current_water*0.3
        current_energy+=0.05*current_energy
        day_for_water=0
    
    day_for_food += 1
    if day_for_food % 3 == 0:
        food_used = current_food/players_num
        current_food-=food_used
        current_energy+=0.1*current_energy
        day_for_food=0

    if current_energy <= 0:
        print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
        break

else:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")