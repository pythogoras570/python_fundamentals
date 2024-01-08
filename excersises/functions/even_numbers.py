sequence = input().split()
numbers = []
for number in sequence:
    numbers.append(int(number))
# numbers = [int(number) for number in numbers] same thing, done with list comprehension instead of for cycle

filtering = lambda x: x % 2 == 0
result = list(filter(filtering, numbers))
print(result)
