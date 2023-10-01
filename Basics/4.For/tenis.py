import math
tournirs_number = int(input())
starting_points = int(input())
won_tournirs = 0
sum_of_points=0
w_final_points = 0
f_final_points = 0
sf_final_points = 0


for i in range(0,tournirs_number):
    type = input()
    
    if type=="W":
        w_final_points = w_final_points+2000
        won_tournirs = won_tournirs +1
    elif type == "F":
        f_final_points = f_final_points + 1200
    elif type == "SF":
        sf_final_points = sf_final_points + 720

sum_of_points =w_final_points + f_final_points + sf_final_points  

final_points = starting_points + sum_of_points

avg_points = sum_of_points/tournirs_number

percent_won = (won_tournirs/tournirs_number) *100

print(f"Final points: {final_points}")
print(F"Average points: {math.floor(avg_points)}")
print(f"{percent_won:.2f}%")