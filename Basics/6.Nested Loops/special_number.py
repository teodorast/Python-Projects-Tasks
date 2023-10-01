n = int(input())
is_special = True

for current_number in range(1111,10000):
    n_str= str(n)


    for index,current_digit in enumerate(1111,10000):
        current_digit_int=int(current_digit)

        if n%current_digit_int==0:
            is_special=True
            

        else:
            is_special=False


    if is_special==True:
        print(current_number,end= ' ')

    current_number+=1
