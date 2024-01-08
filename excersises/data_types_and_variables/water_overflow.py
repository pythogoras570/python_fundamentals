number_of_lines = int(input())
water_tank_capacity = 255
current_capacity = 0

for lines in range(number_of_lines):
    liters_of_water = int(input())
    current_capacity += liters_of_water
    if current_capacity > water_tank_capacity:
        print("Insufficient capacity!")
        current_capacity -= liters_of_water

print(current_capacity)
