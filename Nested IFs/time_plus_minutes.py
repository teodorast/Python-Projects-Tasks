hours = int(input())
minutes = int(input())
final_hours = 0
final_minutes = 0
if minutes >= 45:
    if hours == 23:
        final_hours = 0
        final_minutes = (minutes + 15) % 60
    else:
        final_hours = hours + 1
        final_minutes = (minutes + 15) % 60
else:
    final_hours = hours
    final_minutes = (minutes + 15) % 60


if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else: 
    print(f'{final_hours}:{final_minutes}')