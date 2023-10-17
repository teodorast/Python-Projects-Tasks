n = int(input())
numbers = []
filtered = []


for i in range(n):
    nums = int(input())
    numbers.append(nums)

command = input()

if command == "even":
    for n in numbers:
        if n%2 == 0:
            filtered.append(n)
elif command == "odd":
    for n in numbers:
        if n%2 != 0:
            filtered.append(n)
elif command == "negative":
    for n in numbers:
        if n< 0:
            filtered.append(n)
elif command == "positive":
    for n in numbers:
        if n>= 0:
            filtered.append(n)
print(filtered)