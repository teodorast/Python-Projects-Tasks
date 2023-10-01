group_number = int(input())
musala_people= 0
monblan_people = 0
kili_people=0
k2_people = 0
everest_people = 0
sum = 0
for i in range (0,group_number):
    people_count = int(input())
    sum = sum+people_count

    if people_count<=5:
        musala_people = musala_people + people_count
        
    elif people_count>=6 and people_count<=12:
        monblan_people = monblan_people + people_count

    elif people_count>12 and people_count<=25:
        kili_people = kili_people + people_count

    elif people_count>25 and people_count<=40:
        k2_people = k2_people + people_count

    elif people_count>40:
        everest_people = everest_people + people_count


musala_percent = (musala_people/sum)*100
monblan_percent = (monblan_people/sum)*100
kili_percent = (kili_people/sum)*100
k2_percent = (k2_people/sum)*100
everest_percent = (everest_people/sum)*100


print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kili_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")