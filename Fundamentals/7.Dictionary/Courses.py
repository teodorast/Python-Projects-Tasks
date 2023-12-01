courses = {}

while True:
    input_line = input()
    if input_line == "end":
        break

    course,student = input_line.split(" : ")
    

    if course not in courses:
        courses[course]= []

    courses[course].append(student)

for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")
    

    for student_name in registered_students:
        print(f"-- {student_name}")      


        

