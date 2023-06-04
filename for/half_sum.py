counter = int(input())
sum = 0
for i in range(counter):
    sum = sum + int(input())
    if i == sum:
        print("Yes")
        print(f"Sum = {sum}")




