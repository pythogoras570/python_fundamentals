def sum_numbers(func_number1, func_number2):
    sum_of_numbers = func_number1 + func_number2
    return sum_of_numbers


def subtract(returned_result, func_number3):
    difference = returned_result - func_number3
    return difference


def add_and_subtract(number1, number2, number3):
    result1 = sum_numbers(number1, number2)
    result2 = subtract(result1, number3)
    return result2

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(f'{add_and_subtract(first_number, second_number, third_number)}')
