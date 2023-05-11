hours = int(input())
minutes = int(input())

if minutes >= 45:
    hours =hours + 1
    minutes = (minutes + 15) % 60
else:
    minutes = (minutes + 15) % 60
