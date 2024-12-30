class Shoe:
    def __init__(self, shoe_type, category, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.category = category
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return (f"Тип взуття: {self.shoe_type}, Категорія: {self.category}, Колір: {self.color}, "
                f"Ціна: {self.price}, Виробник: {self.manufacturer}, Розмір: {self.size}")

class ShoeView:
    @staticmethod
    def display_shoe_details(shoe):
        print("\nДеталі взуття:")
        print(shoe)

    @staticmethod
    def display_all_shoes(shoes):
        print("\nУсе взуття:")
        for shoe in shoes:
            print(shoe)

class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe_type, category, color, price, manufacturer, size):
        new_shoe = Shoe(shoe_type, category, color, price, manufacturer, size)
        self.shoes.append(new_shoe)
        return new_shoe

    def get_shoe(self, index):
        if 0 <= index < len(self.shoes):
            return self.shoes[index]
        else:
            raise IndexError("Взуття не знайдено.")

    def get_all_shoes(self):
        return self.shoes

if __name__ == "__main__":
    controller = ShoeController()
    view = ShoeView()

    shoe1 = controller.add_shoe("Чоловіче", "Кросівки", "Чорний", 100, "Nike", 42)
    shoe2 = controller.add_shoe("Жіноче", "Чоботи", "Коричневий", 150, "Timberland", 38)

    view.display_shoe_details(shoe1)

    all_shoes = controller.get_all_shoes()
    view.display_all_shoes(all_shoes)