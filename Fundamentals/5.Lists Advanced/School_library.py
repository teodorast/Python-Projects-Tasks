shelf = input().split("&")

while True:
    command = input().split(" | ")

    if command[0] =="Done":
        break

    action = command[0]
    book_name = command[1]
    if action == "Add Book":

        if book_name not in shelf:
            shelf.insert(0, book_name) 

    elif action == "Take Book":

        if book_name in shelf:
            shelf.remove(book_name)  

    elif action == "Swap Books":

        book_name_2 = command[2]
        if book_name in shelf and book_name_2 in shelf:
            index = shelf.index(book_name)
            index_2=shelf.index(book_name_2)
            shelf[index],shelf[index_2] = shelf[index_2],shelf[index]

    elif action == "Insert Book":

        if book_name not in shelf:
            shelf.append(book_name)  

    elif action == "Check Book":

            book_index = int(command[1])

            if book_index >= 0 and book_index< len(shelf):
                print(shelf[book_index])


print(", ".join(shelf))