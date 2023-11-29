elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    bakery[key]= int(value)


searched_products = input().split()

for p in searched_products:
    if p in bakery:
        print(f"We have {bakery[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")