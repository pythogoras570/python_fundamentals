def sorting(list1):
    list1 = [int(number) for number in list1]
    return sorted(list1)


numbers = input().split()

print(sorting(numbers))
