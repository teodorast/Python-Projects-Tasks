import math

series = input()
series_duration = int(input())
duration = int(input())

time_left = duration - (duration*(1/8)) - (duration*(1/4))

diff = time_left - series_duration

if diff>=0:
    print(f"You have enough time to watch {series} and left with {math.ceil(diff)} minutes free time.")
   
elif diff<0:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(abs(diff))} more minutes.")
   
