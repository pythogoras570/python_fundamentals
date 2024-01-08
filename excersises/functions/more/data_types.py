def data_type(user_input):
    if user_input == "int":
        current_input = int(input())
        return current_input * 2
    elif user_input == "real":
        current_input = float(input())
        return f'{(current_input * 1.5):.2f}'
    elif user_input == "string":
        current_input = input()
        new_string = '$' + current_input + '$'
        return new_string


first_line = input()
print(data_type(first_line))
