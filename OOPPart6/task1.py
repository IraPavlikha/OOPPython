class Shoe:
    def __init__(self, shoe_type, style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.style = style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return (f"Тип: {self.shoe_type}, Вид: {self.style}, Колір: {self.color}, "
                f"Ціна: {self.price} грн, Виробник: {self.manufacturer}, Розмір: {self.size}")

class ShoeView:
    @staticmethod
    def display_shoe_details(shoe):
        print("\nДеталі взуття:")
        print(shoe)

    @staticmethod
    def display_all_shoes(shoes):
        print("\nСписок усіх доступних моделей взуття:")
        for index, shoe in enumerate(shoes, start=1):
            print(f"{index}. {shoe}")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_input(prompt):
        return input(prompt)

class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self):
        shoe_type = ShoeView.get_input("Введіть тип взуття (чоловіче/жіноче): ")
        style = ShoeView.get_input("Введіть вид взуття (кросівки, чоботи тощо): ")
        color = ShoeView.get_input("Введіть колір взуття: ")
        price = float(ShoeView.get_input("Введіть ціну взуття: "))
        manufacturer = ShoeView.get_input("Введіть виробника взуття: ")
        size = int(ShoeView.get_input("Введіть розмір взуття: "))

        new_shoe = Shoe(shoe_type, style, color, price, manufacturer, size)
        self.shoes.append(new_shoe)
        ShoeView.display_message("Нова модель взуття успішно додана!")

    def get_shoe_details(self):
        try:
            index = int(ShoeView.get_input("Введіть номер моделі взуття для перегляду: ")) - 1
            if 0 <= index < len(self.shoes):
                ShoeView.display_shoe_details(self.shoes[index])
            else:
                ShoeView.display_message("Помилка: Модель взуття не знайдена.")
        except ValueError:
            ShoeView.display_message("Помилка: Введіть коректний номер.")

    def show_all_shoes(self):
        if self.shoes:
            ShoeView.display_all_shoes(self.shoes)
        else:
            ShoeView.display_message("Список взуття порожній.")

if __name__ == "__main__":
    controller = ShoeController()

    while True:
        print("\nМеню:")
        print("1. Додати нове взуття")
        print("2. Показати всі моделі взуття")
        print("3. Переглянути деталі конкретної моделі")
        print("4. Вийти")
        choice = ShoeView.get_input("Виберіть опцію (1-4): ")
        if choice == "1":
            controller.add_shoe()
        elif choice == "2":
            controller.show_all_shoes()
        elif choice == "3":
            controller.get_shoe_details()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")