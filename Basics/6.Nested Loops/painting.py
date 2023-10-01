painting_number = int(input())
wallpaper_number= int(input())
gloves_price = float(input())
brush_price = float(input())

import math

total_paint = painting_number*21.50
total_wallpaper = wallpaper_number*5.20
total_gloves = math.ceil((wallpaper_number*0.35)) * gloves_price
total_brush = math.floor(painting_number*0.48) * brush_price




total_price = total_paint+total_wallpaper+total_gloves+total_brush
delivery_price = total_price/15

print(f"This delivery will cost {delivery_price:.2f} lv.")