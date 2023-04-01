lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume=lenght*width*height/1000
liters_needed = volume *  (1 - (percent/100))
print(liters_needed)
