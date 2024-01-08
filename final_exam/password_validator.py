password = input()
while True:
    command = input().split(' ')
    command_type = command[0]
    if command_type == 'Complete':
        break
    elif command_type == 'Make':
        index = int(command[2])
        if command[1] == 'Upper':
            if index in range(len(password)):
                password = password[:index] + password[index].upper() + password[index+1:]
                print(password)
        elif command[1] == 'Lower':
            if index in range(len(password)):
                password = password[:index] + password[index].lower() + password[index+1:]
                print(password)
    elif command_type == 'Insert':
        index = int(command[1])
        char = command[2]
        if index in range(len(password)):
            password = password[:index] + char + password[index:]
            print(password)
    elif command_type == 'Replace':
        char = command[1]
        value = int(command[2])
        new_char = chr(ord(char) + value)
        if char in password:
            password = password.replace(char, new_char)
            print(password)
    elif command_type == 'Validation':
        if len(password) < 8:
            print('Password must be at least 8 characters long!')
        if not all('a' <= c.lower() <= 'z' or '0' <= c <= '9' or c == '_' for c in password):
            print('Password must consist only of letters, digits and _!')
        if not any(c.isupper() for c in password):
            print('Password must consist at least one uppercase letter!')
        if not any(c.islower() for c in password):
            print('Password must consist at least one lowercase letter!')
        if not any(c.isdigit() for c in password):
            print('Password must consist at least one digit!')