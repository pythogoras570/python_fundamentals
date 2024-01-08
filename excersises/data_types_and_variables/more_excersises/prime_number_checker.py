number = int(input())

if number <= 1:
    is_prime_number = False
else:
    is_prime_number = True
    for i in range(2, number):
        if number % i == 0:
            is_prime_number = False
            break

print(is_prime_number)