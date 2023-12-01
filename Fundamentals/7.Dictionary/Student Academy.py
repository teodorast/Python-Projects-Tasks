students = {}
n = int(input())

for i in range(n):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)   

filtered_students = {name: grade for name, grade in students.items() if sum(grade)/len(grade)>=4.50}

for name, score in filtered_students.items():
    average_grade = float(sum(score)/len(score))
    print(f"{name} -> {average_grade:.2f}")

