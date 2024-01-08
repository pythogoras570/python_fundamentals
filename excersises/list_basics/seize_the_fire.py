cells = input().split('#')
water = int(input())
effort = 0
total_fires = 0
fire_out_cells = []
high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)

for cell in cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == 'High':
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == 'Medium':
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == 'Low':
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if water >= cell_value:
            water -= cell_value
            effort += cell_value * 0.25
            fire_out_cells.append(cell_value)
            total_fires += cell_value

print('Cells:')
for fire_out_cell in fire_out_cells:
    print(f'- {fire_out_cell}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fires}")
