phonebook = {}
while True:
    entry = input()

    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name]=phone
seraches = int(entry)

for search in range (seraches):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
