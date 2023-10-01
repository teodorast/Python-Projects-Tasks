counter = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(counter):
    num = int(input())
    if num <200:
        p1_count = p1_count+1
    elif num < 400:
        p2_count = p2_count+1
    elif num < 600:
        p3_count = p3_count+1
    elif num < 800:
        p4_count = p4_count+1
    elif num >= 800:
        p5_count = p5_count+1

p1_percent = p1_count/counter *100
p2_percent = p2_count/counter *100
p3_percent = p3_count/counter *100
p4_percent = p4_count/counter *100
p5_percent = p5_count/counter *100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")