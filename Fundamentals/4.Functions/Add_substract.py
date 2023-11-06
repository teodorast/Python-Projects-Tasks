def sum_numbers(first,second):
    return first+second



def subtract(res,third_num):
    return res - third_num


def sum_and_subtract(first_num,second_num,third_num):
    first_secondsum= sum_numbers(first_num,second_num)
    result = subtract(first_secondsum,third_num)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(sum_and_subtract(first_number,second_number,third_number))


    
