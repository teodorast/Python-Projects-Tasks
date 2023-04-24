flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    if number_of_flowers > 80:
        price = (number_of_flowers * 5) - (number_of_flowers * 5* 0.1)
    else:
        price = (number_of_flowers * 5)


elif flower_type == "Dahlias":
    if number_of_flowers > 90:
        price = (number_of_flowers * 3.80)- (number_of_flowers * 3.80* 0.15)
    else:   
        price = number_of_flowers * 3.80


elif flower_type == "Tulips":
    if number_of_flowers > 80:
        price = (number_of_flowers * 2.8) - (number_of_flowers * 2.80* 0.15)
    else:
        price = (number_of_flowers * 2.8)

elif flower_type == "Narcissus":
    if number_of_flowers <120:
        price = (number_of_flowers * 3) + (number_of_flowers * 3* 0.15)
    else:
        price = (number_of_flowers * 3)

elif flower_type == "Gladiolus":
    if number_of_flowers < 80:
        price = (number_of_flowers * 2.50) + (number_of_flowers * 2.50* 0.2)
    else: 
         price = (number_of_flowers * 2.50)

summary = budget - price        
if summary >= 0 :
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {summary:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(summary):.2f} leva more.")