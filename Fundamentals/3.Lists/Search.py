n = int(input())
key_word = input()
my_list = []

for i in range(n):
    word = input()
    my_list.append(word)
print(my_list)

for j in range(len(my_list)-1,-1,-1):
    element = my_list[j]
    if key_word not in element: 
        my_list.remove(element)

print(my_list)

