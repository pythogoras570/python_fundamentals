def smallest_int(some_numbers):
    smallest = min(some_numbers)
    return smallest

first_number = int(input())
second_number = int(input())
third_number = int(input())
number = [first_number, second_number, third_number]

print(f'{smallest_int(number)}')
