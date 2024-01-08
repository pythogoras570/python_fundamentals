user_list = input().split()
opposite_user_list = []

for number in user_list:
    current_number = -int(number)
    opposite_user_list.append((current_number))
print(opposite_user_list)
