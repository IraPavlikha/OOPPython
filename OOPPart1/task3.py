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
        print("\nОновлення інформації про стадіон (Щоб зберегти поточне значення,залиште поле порожнім):")
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

if __name__ == "__main__":
    stadium = Stadium(
        name="Олімпійський стадіон",
        opening_date="12 липня 1980",
        country="Україна",
        city="Київ",
        capacity=70050
    )

    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про стадіон")
        print("2. Оновити інформацію про стадіон")
        print("3. Вийти")

        choice = input("Ваш вибір: ")
        if choice == "1":
            stadium.display_info()
        elif choice == "2":
            stadium.update_info()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")