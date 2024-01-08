numbers = input().split()
numbers_list = []

for num in numbers:
    numbers_list.append(abs(float(num)))

print(numbers_list)
