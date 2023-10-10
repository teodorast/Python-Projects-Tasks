years = int(input())
year_is_special = False
while not year_is_special:
    years+=1
    year_is_special=True
    years_as_string=str(years)
    for digit in (years_as_string):
        if years_as_string.count(digit)!=1:
            year_is_special=False
            break
print(years_as_string)

