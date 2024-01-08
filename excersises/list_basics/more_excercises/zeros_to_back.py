def zeros_back(lists):
    no_zero_list = []
    for i in range(len(lists)):
        if lists[i] != '0':
            no_zero_list.append(lists[i])
    zero_count = len(lists) - len(no_zero_list)
    for i in range(zero_count):
        no_zero_list.append('0')
    print(f'[{", ".join(no_zero_list)}]')


user_input = input().split(', ')
zeros_back(user_input)
