open_tabs = int(input())
salary = int(input())
facebook_count = 0
instagram_count = 0
reddit_count = 0

for i in range(0,open_tabs):
    site = input()
    if site == "Facebook":
        
        salary = salary - 150

        if salary<=0:
            print("You have lost your salary.")
            break
    elif site == "Instagram":
        
        salary = salary - 100
        if salary<=0:
            print("You have lost your salary.")
            break
    elif site == "Reddit":
     
        salary = salary - 50
        if salary<=0:
            print("You have lost your salary.")
            break
if salary>0:

    print(salary)
