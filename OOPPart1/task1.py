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
        print("\nОновлення інформації про автомобіль (Щоб зберегти поточне значення,залиште поле порожнім):")
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
if __name__ == "__main__":
    car = Car(
        model="Tesla",
        year=2024,
        manufacturer="Tesla",
        engine_volume=0.0,
        color="Black",
        price=1500000
    )
    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про автомобіль")
        print("2. Оновити інформацію про автомобіль")
        print("3. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            car.display_info()
        elif choice == "2":
            car.update_info()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")