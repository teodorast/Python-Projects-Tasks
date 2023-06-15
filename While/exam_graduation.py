max_fails = int(input())
fail_counter = 0
task_counter = 0
last_task_name=""
sum_score = 0


while True:
    user_command = input()

    if user_command=="Enough":
        break

    last_task_name = user_command
    current_task_score = int(input())
   
    sum_score+=current_task_score
    task_counter+=1
    average_score = sum_score/task_counter

    if current_task_score<=4:
        fail_counter+=1

        if fail_counter>=max_fails:
            break

if user_command=="Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task_name}")
    
else:
     print(f"You need a break, {max_fails} poor grades.")

