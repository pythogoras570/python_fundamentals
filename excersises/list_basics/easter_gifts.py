gift_list = input().split(" ")
current_command = input()
required_list = []

while current_command != "No Money":
    if 'OutOfStock' in current_command:
        new_command = current_command.replace('OutOfStock ', '')
        gift_list = [None if item == new_command else item for item in gift_list]
    elif 'Required' in current_command:
        new_command = current_command.replace('Required ', '')
        new_list = new_command.split(' ')
        var = int(new_list[1])
        varb = len(gift_list)
        if varb >= var:
            gift_list[int(new_list[1])] = new_list[0]
    elif 'JustInCase' in current_command:
        new_command = current_command.replace('JustInCase ', '')
        gift_list.pop(len(gift_list) -1)
        new_list = [new_command]
        gift_list.extend(new_list)
    current_command = input()

for items in gift_list:
    if items is None:
        gift_list.remove(items)

print(*gift_list, sep=' ')
