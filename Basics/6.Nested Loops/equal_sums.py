first_number = int(input())
second_number = int(input())



for current_number in range(first_number, second_number+1):
    current_number_str= str(current_number)
    sum_odd = 0
    sum_even = 0

    for index,current_digit in enumerate(current_number_str):

        if index%2==0:
            sum_odd = sum_odd+int(current_digit)

        else:
            sum_even+=int(current_digit)


    if sum_even==sum_odd:
        print(current_number,end= ' ')

        current_number+=1



        
