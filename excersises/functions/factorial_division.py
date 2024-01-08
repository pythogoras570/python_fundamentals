def factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


n = int(input())
n1 = int(input())
n_factorial = factorial(n)
n1_factorial = factorial(n1)

print(f'{(n_factorial / n1_factorial):.2f}')
