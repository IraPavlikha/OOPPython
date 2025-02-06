basketball_players = {}

def add_player(name, height):
    basketball_players[name] = height
    print(f"Додано: {name} з ростом {height} см")

def remove_player(name):
    if name in basketball_players:
        del basketball_players[name]
        print(f"Видалено: {name}")
    else:
        print("Гравця не знайдено.")

def find_player(name):
    return basketball_players.get(name, "Гравця не знайдено.")

def update_player(name, new_height):
    if name in basketball_players:
        basketball_players[name] = new_height
        print(f"Оновлено: {name} тепер має зріст {new_height} см")
    else:
        print("Гравця не знайдено.")

def show_all_players():
    if basketball_players:
        print("Список баскетболістів:")
        for name, height in basketball_players.items():
            print(f"{name}: {height} см")
    else:
        print("Список порожній.")

add_player("Майкл Джордан", 198)
add_player("Леброн Джеймс", 206)
show_all_players()
update_player("Леброн Джеймс", 207)
print(find_player("Майкл Джордан"))
remove_player("Майкл Джордан")
show_all_players()