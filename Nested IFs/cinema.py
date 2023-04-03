movie_type = input()
r = int(input())
c = int(input())
income = 0
if movie_type == "Premiere":
    income = r*c*12
elif movie_type == "Normal":
    income = r*c*7.5
elif movie_type == "Discount":
    income = r*c*5
print(f"{income:.2f} leva")