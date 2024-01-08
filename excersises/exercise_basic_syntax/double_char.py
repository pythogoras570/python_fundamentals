user_input = input()

while user_input != "End":
    if user_input != "SoftUni":
        new_string = ""
        for character in user_input:
            new_string += character * 2
        print(new_string)

    user_input = input()
