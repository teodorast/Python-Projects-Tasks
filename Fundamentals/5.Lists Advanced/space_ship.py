

route = input()
commands = route.split('||')
fuel = int(input())  
ammo = int(input())
for command in commands:
    command = command.strip().split()
    action = command[0]

    if action == 'Travel':
        distance = int(command[1])
        required_fuel = distance
        if fuel >= required_fuel:
            fuel -= required_fuel
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif action == 'Enemy':
        enemy_armor = int(command[1])
        if ammo >= enemy_armor:
            ammo -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            required_fuel = enemy_armor * 2
            if fuel >= required_fuel:
                fuel -= required_fuel
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif action == 'Repair':
        ammo_added = int(command[1])
        fuel_added = int(command[1])
        ammo += ammo_added * 2
        fuel += fuel_added
        print(f"Ammunitions added: {ammo_added*2}.")
        print(f"Fuel added: {fuel_added}.")

    elif action == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break


if "Titan" not in route:
    print("Mission failed.")