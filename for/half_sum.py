counter = int(input())
max_element = -1828717717723
sum_number = 0

for i in range(counter):
    num = int(input())
    sum_number = sum_number + num

    if num > max_element:
        max_element = num 

    new_sum = sum_number - max_element
if max_element == sum_number - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else: 
    print("No")
    print(f"Diff = {abs(max_element-new_sum)}")




