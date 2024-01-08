string = input()
capital_indices = [index for index, char in enumerate(string) if char.isupper()]
print(capital_indices)
