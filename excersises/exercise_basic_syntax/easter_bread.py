budget = float(input())
price_flour_kg = float(input())
price_eggs_pack = price_flour_kg * 0.75
price_milk_quarter = (price_flour_kg * 1.25) / 4
colored_eggs = 0
current_bread_count = 0

while True:
    if budget > (price_flour_kg + price_eggs_pack + price_milk_quarter):
        current_bread_count += 1
        colored_eggs += 3
        budget -= (price_flour_kg + price_eggs_pack + price_milk_quarter)
        if current_bread_count % 3 == 0:
            colored_eggs -= (current_bread_count - 2)
    else:
        break

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


