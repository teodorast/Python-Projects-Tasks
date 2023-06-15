record = float(input())
meters = float(input())
time = float(input())

ivan_time = meters * time
delay = (meters//15) * 12.5

total_time = ivan_time + delay
difference = record - total_time
if difference > 0:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif difference <=0:
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")