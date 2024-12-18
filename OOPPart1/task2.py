class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"\nІнформація про книгу:")
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавництво: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price} грн")

    def update_info(self):
        print("\nОновлення інформації про книгу (Щоб зберегти поточне значення,залиште поле порожнім):")
        title = input(f"Назва ({self.title}): ")
        if title:
            self.title = title
        year = input(f"Рік видання ({self.year}): ")
        if year:
            self.year = int(year)
        publisher = input(f"Видавництво ({self.publisher}): ")
        if publisher:
            self.publisher = publisher
        genre = input(f"Жанр ({self.genre}): ")
        if genre:
            self.genre = genre
        author = input(f"Автор ({self.author}): ")
        if author:
            self.author = author
        price = input(f"Ціна ({self.price} грн): ")
        if price:
            self.price = float(price)

if __name__ == "__main__":
    book = Book(
        title="Майстер і Маргарита",
        year=1967,
        publisher="Азбука",
        genre="Роман",
        author="Михайло Булгаков",
        price=300
    )

    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про книгу")
        print("2. Оновити інформацію про книгу")
        print("3. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            book.display_info()
        elif choice == "2":
            book.update_info()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")