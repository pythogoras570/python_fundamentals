import sys

numbers_list = input().split(" ")
numbers_to_remove = int(input())
int_number_list = []
numbers_removed = 0
number_counter = -9999

for number in numbers_list:
    int_number_list.append(int(number))

while numbers_removed < numbers_to_remove:
    if number_counter in int_number_list:
        int_number_list.remove(number_counter)
        number_counter = 0
        numbers_removed += 1
    else:
        number_counter += 1

print(*int_number_list, sep=', ')

