product=input()
quantity = int(input())
total_price = 0

def total_price(prod,qu):
    if product=="coffee":
        total_price = quantity*1.50
    elif product == "coke":
        total_price = quantity*1.40
    elif product == "water":
        total_price = quantity*1
    elif product == "snacks":
        total_price = quantity*2
    
    return(total_price)

result = total_price(product,quantity)
print(f"{result:.2f}")