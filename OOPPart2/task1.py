class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        print(f"\nІнформація про автомобіль:")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} грн")

    def update_info(self):
        print("\nОновлення інформації про автомобіль (Щоб зберегти поточне значення, залиште поле порожнім):")
        model = input(f"Модель ({self.model}): ")
        if model:
            self.model = model
        year = input(f"Рік випуску ({self.year}): ")
        if year:
            self.year = int(year)
        manufacturer = input(f"Виробник ({self.manufacturer}): ")
        if manufacturer:
            self.manufacturer = manufacturer
        engine_volume = input(f"Об'єм двигуна ({self.engine_volume} л): ")
        if engine_volume:
            self.engine_volume = float(engine_volume)
        color = input(f"Колір ({self.color}): ")
        if color:
            self.color = color
        price = input(f"Ціна ({self.price} грн): ")
        if price:
            self.price = float(price)

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}), {self.engine_volume} л, {self.color}, {self.price} грн"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (self.model == other.model and
                self.year == other.year and
                self.manufacturer == other.manufacturer and
                self.engine_volume == other.engine_volume and
                self.color == other.color and
                self.price == other.price)

    def __lt__(self, other):
        return self.price < other.price

if __name__ == "__main__":
    car1 = Car(
        model="Tesla Model S",
        year=2024,
        manufacturer="Tesla",
        engine_volume=0.0,
        color="Black",
        price=1500000
    )

    car2 = Car(
        model="Ford Mustang",
        year=2020,
        manufacturer="Ford",
        engine_volume=5.0,
        color="Red",
        price=1200000
    )

    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про автомобіль")
        print("2. Оновити інформацію про автомобіль")
        print("3. Порівняти автомобілі")
        print("4. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            car1.display_info()
        elif choice == "2":
            car1.update_info()
        elif choice == "3":
            print("\nПорівняння автомобілів:")
            print(f"Автомобіль 1: {car1}")
            print(f"Автомобіль 2: {car2}")
            print("Одинкові" if car1 == car2 else "Різні")
            print("Автомобіль 1 дешевший" if car1 < car2 else "Автомобіль 2 дешевший")
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")