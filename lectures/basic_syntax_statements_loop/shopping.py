budget = int(input())
total_price = 0

while True:
    user_input = (input())

    if user_input == 'End':
        print('You bought everything needed')
        break

    price = int(user_input)

    if total_price + price > budget:
        print('You went in overdraft!')
        break

    total_price += price
