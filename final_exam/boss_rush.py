def check_validity(n):
    for _ in range(n):
        data = input()
        if ":" in data:
            boss_name, title = data.split(":")
            if boss_name[0] == "|" and boss_name[-1] == "|" and title[0] == "#" and title[-1] == "#":
                boss_name = boss_name[1:-1]
                title = title[1:-1]
                if boss_name.isupper() and len(boss_name) >= 4 and len(title.split()) == 2 and title.replace(" ", "").isalpha():
                    print(f"{boss_name}, The {title}")
                    print(f">> Strength: {len(boss_name)}")
                    print(f">> Armor: {len(title)}")
                else:
                    print("Access denied!")
            else:
                print("Access denied!")
        else:
            print("Access denied!")

n = int(input())
check_validity(n)
