number_of_snowballs = int(input())
best_snowball = int(0)
best_snowball_weight = 0
best_snowball_time_to_target = 0
best_snowball_quality = 0

for snowballs in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())
    current_snowball_value = int((snowball_weight / snowball_time_to_target) ** snowball_quality)
    if current_snowball_value >= best_snowball:
        best_snowball = current_snowball_value
        best_snowball_weight = snowball_weight
        best_snowball_time_to_target = snowball_time_to_target
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time_to_target} = {best_snowball} ({best_snowball_quality})")
