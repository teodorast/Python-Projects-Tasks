n = int(input())
current_number = 1
is_current_bigger = False


for current_row in range(1,n+1):
    for numer_in_row in range(1, current_row+1):
        if current_number >n:
            is_current_bigger = True
            break
        else:
            print(str(current_number) + ' ', end ='')
            current_number+=1

    if is_current_bigger == True:
        break

    print()

