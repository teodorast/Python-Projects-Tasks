def sum_digits(some_num:str):
    sum_even =0
    sum_odd=0

    for digit in some_num:
        if int(digit)%2==0:
            sum_even+=int(digit)
        else:
            sum_odd += int(digit)
    return sum_odd,sum_even
        

number= input()
sum_of_odd_digits, sum_of_even_digits = sum_digits(number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")