locations = int(input())
average_gold = 0



for i in range(locations):
    expected_gold = float(input())
    days = int(input())

    amount_gold_sum = 0
    for d in range(days):
        amount_gold = float(input())
        amount_gold_sum+=amount_gold

        average_gold = amount_gold_sum/days

    if average_gold>=expected_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
  
    elif average_gold<expected_gold:
        print(f"You need {(expected_gold-average_gold):.2f} gold.")




