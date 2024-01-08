def minimum_number(list1):
    list1 = [int(number) for number in list1]
    minimum = min(list1)
    return minimum


def maximum_number(list2):
    list2 = [int(number) for number in list2]
    maximum = max(list2)
    return maximum


def sum_of_all_numbers(list3):
    list3 = [int(number) for number in list3]
    total = 0
    for number in list3:
        total += number
    return total


numbers = input().split()

print(f"The minimum number is {minimum_number(numbers)}")
print(f"The maximum number is {maximum_number(numbers)}")
print(f"The sum number is: {sum_of_all_numbers(numbers)}")
