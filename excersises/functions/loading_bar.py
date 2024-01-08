def loading_bar(percentage):
    signs = int(percentage / 10)
    bar = []
    for i in range(signs):
        bar.append('%')
    left = 10 - signs
    if left == 0:
        bar_string = ''.join(bar)
        return print(f'{percentage}% Complete!\n[{bar_string}]')
    else:
        for i in range(left):
            bar.append('.')
        bar_string = ''.join(bar)
    return print(f'{percentage}% [{bar_string}]\nStill loading...')


user_input = int(input())
loading_bar(user_input)
