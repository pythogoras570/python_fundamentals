money = input().split(', ')
beggars = int(input())
money_int = []
beggars_income = []
start_index = 0

for turns in money:
    money_int.append(int(turns))

while start_index < beggars:
    sum_current_beggar = 0
    for current_index in range(start_index, len(money_int), beggars):
        sum_current_beggar += money_int[current_index]
    beggars_income.append(sum_current_beggar)
    start_index += 1

print(beggars_income)
