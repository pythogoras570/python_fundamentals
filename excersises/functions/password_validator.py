def password_check(passed_word):
    counter = 0
    valid = True
    if len(passed_word) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        valid = False
    for letter in passed_word:
        if 48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            continue
        else:
            valid = False
            print("Password must consist only of letters and digits")
            break
    for letter in passed_word:
        if ord(letter) in (range(48, 58)):
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        valid = False
    return valid


password = input()
if password_check(password):
    print("Password is valid")
