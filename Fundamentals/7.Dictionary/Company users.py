companies = {}

while True:
    input_line = input()
    if input_line == "End":
        break

    company,employee = input_line.split(" -> ")

    if company not in companies:
        companies[company] = []

    if employee not in companies[company]:
        companies[company].append(employee)

for company, employee in companies.items():
    print(f"{company}")

    for emp in employee:
        print(f"-- {emp}")

