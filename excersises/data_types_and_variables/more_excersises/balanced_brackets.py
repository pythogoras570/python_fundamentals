number_of_lines = int(input())
counter = 0

for lines in range(number_of_lines):
    current_line = input()
    if current_line == '(':
        counter += 1
        if counter == 2:
            break

    elif current_line == ')':
        counter -= 1
        if counter == -1:
            break

if counter != 0:
    print('UNBALANCED')
else:
    print('BALANCED')
