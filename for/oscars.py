actor_name = input()
academy_points = float(input())
jurry_number = int(input())

for i in range (0,jurry_number):
    jurry_name = input()
    jurry_points= float(input())

    academy_points = academy_points + ((len(jurry_name)*jurry_points)/2)

    if academy_points >=1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break


else:
    print(f"Sorry, {actor_name} you need {(1250.5-academy_points):.1f} more!")