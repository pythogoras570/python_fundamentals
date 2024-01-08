n = int(input())
special_chars = ',._'
for check in range(n):
    new_string = input()
    if any(c in special_chars for c in new_string):
        print(f'{new_string} is not pure!')
    else:
        print(f'{new_string} is pure.')

