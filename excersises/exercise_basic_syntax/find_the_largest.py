number = int(input())

digits = list(str(number))
digits.sort(reverse=True)
largest_number = int(''.join(digits))

print(largest_number)