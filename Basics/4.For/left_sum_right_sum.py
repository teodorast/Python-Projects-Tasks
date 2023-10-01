counter = int(input())
left_sum = 0
right_sum = 0
for i in range(1, counter+1):
    left_sum = left_sum+int(input())

for k in range(counter, 2*counter):
    right_sum = right_sum +int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")
