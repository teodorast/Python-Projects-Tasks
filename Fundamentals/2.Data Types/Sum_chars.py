num_chars = int(input())
total_sum = 0
for i in range (num_chars):
    character = input()
    total_sum+=ord(character)


print(f"The sum equals: {total_sum}")
