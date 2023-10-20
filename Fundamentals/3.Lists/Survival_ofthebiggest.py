my_list = input().split()
n = int(input())
min_number = 0

my_list_ints = []

for i in my_list:
    my_list_ints.append(int (i))

for i in range(n):
    my_list_ints.remove(min(my_list_ints))
   
result = ', '.join(map(str, my_list_ints))
print(result)