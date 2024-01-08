user_input = input()
coffees = 0
one_coffees = ["coding", "dog", "cat", "movie"]
two_coffees = ["CODING", "DOG", "CAT", "MOVIE"]

while user_input != "END":
    if user_input.isupper() and user_input in two_coffees:
        coffees += 2
    if user_input.islower() and user_input in one_coffees:
        coffees += 1
    user_input = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
