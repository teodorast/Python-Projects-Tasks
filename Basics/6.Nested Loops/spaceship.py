ship_width = float(input())
ship_lenght=float(input())
ship_height = float(input())
astronauts_height = float(input())

import math

ship_volume=ship_height*ship_lenght*ship_width
room_volume = (astronauts_height+0.40)*2*2

number_astronauts = math.floor((ship_volume/room_volume))

if number_astronauts<3:
    print(f"The spacecraft is too small.")

elif number_astronauts>=3 and number_astronauts<=10:
    print(f"The spacecraft holds {number_astronauts} astronauts." )


else:
    print(f"The spacecraft is too big.")
