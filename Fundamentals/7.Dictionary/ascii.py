characters = input().split(", ")

new_dictionary = {word: ord(word) for word in characters}
print(new_dictionary)
