n = int(input())
for first_symbol in range(n):
    for second_sybmbol in range(n):
        for third_symbol in range(n):
            print(f"{chr(97+first_symbol)}{chr(97+second_sybmbol)}{chr(97+third_symbol)}")