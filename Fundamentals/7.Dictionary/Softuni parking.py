parkings = {}

n = int(input())

for i in range(0,n):
    command= input().split()

    if "register" in command:
        name,car_num = command[1],command[2]

        if name not in parkings:
            parkings[name]= car_num
            print(f"{name} registered {car_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_num}")

    
    elif "unregister" in command:
        name = command[1]

        if name not in parkings:
           
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parkings[name]

for user,car in parkings.items():
    print(f"{user} => {car}")