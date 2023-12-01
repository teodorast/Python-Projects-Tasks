product_dict = {}

while True:
    command = input()
    if command == "buy":
        break

    product_info = command.split()
    name,price,quantity = product_info[0],float(product_info[1]),int(product_info[2])

    if name not in product_dict:

        product_dict[name] = {'price': price, 'quantity': quantity}
    else:
        product_dict[name]['quantity'] += quantity
        if product_dict[name]['price'] != price:
            product_dict[name]['price'] = price


for product, data in product_dict.items():
    total = data['price'] * data['quantity']

    print(f"{product} -> {total:.2f}")





