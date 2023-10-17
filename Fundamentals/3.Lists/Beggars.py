money=input().split(", ")
beggars_count = int(input())
money_num = []
for i in money:
    money_num.append(int(i))

final_sums=[]
start_index = 0 
for b in range(beggars_count):
    current_beggar_sum = 0
    for current_index in range (start_index, len(money_num),beggars_count):
        current_beggar_sum+=money_num[current_index]
    final_sums.append(current_beggar_sum)
    start_index+=1
print(final_sums)
