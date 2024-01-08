def in_between(letter1, letter2):
    int_list = []
    for int_data in range(ord(letter1) + 1, ord(letter2)):
        int_list.append(chr(int_data))
    return ' '.join(int_list)


char1 = input()
char2 = input()

print(in_between(char1, char2))
