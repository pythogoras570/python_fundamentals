class Zoo:
    def __init__(self):
        self.animals = {}
        self.areas = {}

    def add(self, animal_name, needed_food_quantity, area):
        if animal_name not in self.animals:
            self.animals[animal_name] = {'needed_food_quantity': needed_food_quantity, 'area': area}
            if area not in self.areas:
                self.areas[area] = []
            self.areas[area].append(animal_name)
        else:
            self.animals[animal_name]['needed_food_quantity'] += needed_food_quantity

    def feed(self, animal_name, food):
        if animal_name in self.animals:
            self.animals[animal_name]['needed_food_quantity'] -= food
            if self.animals[animal_name]['needed_food_quantity'] <= 0:
                print(f"{animal_name} was successfully fed")
                self.areas[self.animals[animal_name]['area']].remove(animal_name)
                del self.animals[animal_name]

    def end_day(self):
        print("Animals:")
        for animal_name, animal_info in self.animals.items():
            print(f" {animal_name} -> {animal_info['needed_food_quantity']}g")
        print("Areas with hungry animals:")
        for area_name, area_animals in self.areas.items():
            if len(area_animals) > 0:
                print(f" {area_name}: {len(area_animals)}")

zoo = Zoo()

while True:
    command = input()
    if command == 'EndDay':
        zoo.end_day()
        break
    action, data = command.split(': ')
    if action == 'Add':
        animal_name, needed_food_quantity, area = data.split('-')
        zoo.add(animal_name, int(needed_food_quantity), area)
    elif action == 'Feed':
        animal_name, food = data.split('-')
        zoo.feed(animal_name, int(food))
