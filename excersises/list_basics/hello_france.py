items_list = input().split('|')
budget = float(input())
profit = 0
bought_items = []

for each_item in items_list:
    current_item = each_item.split("->")
    type_of_item = current_item[0]
    item_value = float(current_item[1])
    if type_of_item == 'Clothes' and item_value <= 50.00:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.4
            bought_items.append(item_value * 1.4)
    elif type_of_item == 'Shoes' and item_value <= 35.00:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.4
            bought_items.append(item_value * 1.4)
    elif type_of_item == 'Accessories' and item_value <= 20.50:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.4
            bought_items.append(item_value * 1.4)

for bought_item in bought_items:
    print(f'{bought_item:.2f}', end = ' ')
print()
print(f'Profit: {profit:.2f}')

total_income = budget + sum(list(bought_items))
if total_income >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
