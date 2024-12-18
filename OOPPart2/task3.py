class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"\nІнформація про стадіон:")
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} осіб")

    def update_info(self):
        print("\nОновлення інформації про стадіон (Щоб зберегти поточне значення, залиште поле порожнім):")
        name = input(f"Назва ({self.name}): ")
        if name:
            self.name = name
        opening_date = input(f"Дата відкриття ({self.opening_date}): ")
        if opening_date:
            self.opening_date = opening_date
        country = input(f"Країна ({self.country}): ")
        if country:
            self.country = country
        city = input(f"Місто ({self.city}): ")
        if city:
            self.city = city

        capacity = input(f"Місткість ({self.capacity} осіб): ")
        if capacity:
            self.capacity = int(capacity)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country}), відкритий {self.opening_date}, місткість: {self.capacity} осіб"

    def __eq__(self, other):
        if not isinstance(other, Stadium):
            return False
        return (self.name == other.name and
                self.opening_date == other.opening_date and
                self.country == other.country and
                self.city == other.city and
                self.capacity == other.capacity)

    def __lt__(self, other):
        return self.capacity < other.capacity

if __name__ == "__main__":
    stadium1 = Stadium(
        name="Олімпійський стадіон",
        opening_date="12 липня 1980",
        country="Україна",
        city="Київ",
        capacity=70050
    )

    stadium2 = Stadium(
        name="Уемблі",
        opening_date="19 травня 2007",
        country="Англія",
        city="Лондон",
        capacity=90000
    )

    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про стадіон 1")
        print("2. Оновити інформацію про стадіон 1")
        print("3. Порівняти два стадіони")
        print("4. Вийти")

        choice = input("Ваш вибір: ")
        if choice == "1":
            stadium1.display_info()
        elif choice == "2":
            stadium1.update_info()
        elif choice == "3":
            print("\nПорівняння стадіонів:")
            print(f"Стадіон 1: {stadium1}")
            print(f"Стадіон 2: {stadium2}")
            print("Стадіони однакові" if stadium1 == stadium2 else "Стадіони різні")
            print("Стадіон 1 менший за місткістю" if stadium1 < stadium2 else "Стадіон 2 менший за місткістю")
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")