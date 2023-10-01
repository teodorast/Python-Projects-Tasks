judges_number = int(input())
user_command=input()
total_sum_grades=0
total_grades_counter = 0

while user_command!="Finish":
    presentation = user_command

    sum_of_grades=0
    for i in range(judges_number):
        grade = float(input())
        sum_of_grades+=grade

           
    average_grade = sum_of_grades/judges_number
    total_sum_grades+=sum_of_grades
    total_grades_counter+=1

    print(f"{presentation} - {average_grade:.2f}.")

    user_command=input()

total_avg = total_sum_grades/(total_grades_counter*judges_number)

print(f"Student's final assessment is {total_avg:.2f}.")

