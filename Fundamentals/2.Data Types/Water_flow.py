capacity = 255
flows_number = int(input())
water_counter = 0 

for i in range(flows_number):
    liters_water = int(input())

    if capacity - liters_water<0:
        print("Insufficient capacity!")

        continue

    capacity -= liters_water
    water_counter+=liters_water

print(water_counter)