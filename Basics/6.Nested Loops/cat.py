cat_type = input()
gender = input()
cath_months = 0
import math


if cat_type=="British Shorthair":
    if gender =="m":
        cat_months = math.floor((13*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((14*12)/6)
        print(f"{cat_months} cat months")

elif cat_type=="Siamese":
    if gender =="m":
        cat_months = math.floor((15*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((16*12)/6)
        print(f"{cat_months} cat months")

elif cat_type=="Persian":
    if gender =="m":
        cat_months = math.floor((14*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((15*12)/6)
        print(f"{cat_months} cat months")


elif cat_type=="Ragdoll":
    if gender =="m":
        cat_months = math.floor((16*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((17*12)/6)
        print(f"{cat_months} cat months")


elif cat_type=="American Shorthair":
    if gender =="m":
        cat_months = math.floor((12*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((13*12)/6)
        print(f"{cat_months} cat months")

elif cat_type=="Siberian":
    if gender =="m":
        cat_months = math.floor((11*12)/6)
        print(f"{cat_months} cat months")
    elif gender =="f":
        cat_months = math.floor((12*12)/6)
        print(f"{cat_months} cat months")

else:
    print(f"{cat_type} is invalid cat!")