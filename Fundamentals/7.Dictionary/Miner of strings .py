resources = {}

while True:
    current_resourses = input()
    if current_resourses == "stop":
        break 

    current_quantity = int(input())

    if current_resourses not in resources.keys():
        resources[current_resourses] = 0
    resources[current_resourses]+=current_quantity


for resource,quantity in resources.items():
    print(f"{resource} -> {quantity}")
