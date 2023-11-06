nums_str=input().split()
nums_ints=[]

for num in nums_str:
    nums_ints.append(int(num))


min_n = lambda x:min(x)
max_n = lambda x:max(x)
sums = lambda x:sum(x)


min_result = min_n(nums_ints)
max_result = max_n(nums_ints)
sum_result = sums(nums_ints)

print(f"The minimum number is {min_result}")
print(f"The maximum number is {max_result}")
print(f"The sum number is: {sum_result}")