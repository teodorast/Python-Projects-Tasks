def ranged(a,b):
    list_helper = []
    for i in range (ord(a)+1, ord(b)):
        list_helper.append(chr(i))
    return list_helper

first_char=input()
second_char=input()

result = ranged(first_char,second_char)
print(" ".join(result))