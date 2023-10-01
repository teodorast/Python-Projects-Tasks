counter = int(input())
odd_sum = 0
even_sum = 0
for i in range(counter):
    if i %2 ==0:
        even_sum = even_sum+int(input())
    else:
        odd_sum = odd_sum+int(input())
if odd_sum==even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum-even_sum)}")