def perfect_number(n):
    totals = 0
    for i in range(1, n):
        if n % i == 0:
            totals += i
    if totals == n:
        return True
    else:
        return False


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
