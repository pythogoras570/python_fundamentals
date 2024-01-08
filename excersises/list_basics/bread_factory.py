initial_energy = 100
initial_coins = 100
events = input().split('|')
factory_open = True

for each_event in events:
    current_event = each_event.split("-")
    type_of_event = current_event[0]
    event_value = int(current_event[1])
    if type_of_event == 'rest':
        event_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - event_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_of_event == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_open = False
            print(f"Closed! Cannot afford {type_of_event}.")
            break

if factory_open:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")
