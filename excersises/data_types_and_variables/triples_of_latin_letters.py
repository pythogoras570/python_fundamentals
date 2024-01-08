user_input = int(input())

for char1 in range(0, user_input):
    for char2 in range(0, user_input):
        for char3 in range(0, user_input):
            print(f"{chr(97 + char1)}{chr(97 + char2)}{chr(97 + char3)}")