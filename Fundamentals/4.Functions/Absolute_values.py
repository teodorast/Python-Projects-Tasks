my_list = input().split()
my_list_ints=[]


for nums in my_list: 
    my_list_ints.append(abs(float(nums)))

print(my_list_ints)
