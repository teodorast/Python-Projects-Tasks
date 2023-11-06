nums_str=input().split()
nums_ints=[]

for num in nums_str:
    nums_ints.append(int(num))

sorting = lambda x: sorted(x)
result = sorting(nums_ints)
print(result)