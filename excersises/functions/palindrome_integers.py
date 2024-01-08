def palindrome_check(list1):
    for i in list1:
        reverse = i[::-1]
        if i == reverse:
            print('True')
        else:
            print('False')
    return


list_of_integers = input().split(', ')
palindrome_check(list_of_integers)
