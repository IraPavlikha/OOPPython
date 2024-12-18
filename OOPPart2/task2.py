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
        print("\nОновлення інформації про книгу (Щоб зберегти поточне значення, залиште поле порожнім):")
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

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), {self.genre}, {self.publisher}, {self.price} грн"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.year == other.year and
                self.publisher == other.publisher and
                self.genre == other.genre and
                self.author == other.author and
                self.price == other.price)

    def __lt__(self, other):
        return self.price < other.price

if __name__ == "__main__":
    book1 = Book(
        title="Майстер і Маргарита",
        year=1967,
        publisher="Азбука",
        genre="Роман",
        author="Михайло Булгаков",
        price=300
    )

    book2 = Book(
        title="1984",
        year=1949,
        publisher="Penguin Books",
        genre="Антиутопія",
        author="Джордж Орвелл",
        price=250
    )

    while True:
        print("\nОберіть дію:")
        print("1. Вивести інформацію про книгу")
        print("2. Оновити інформацію про книгу")
        print("3. Порівняти книги")
        print("4. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            book1.display_info()
        elif choice == "2":
            book1.update_info()
        elif choice == "3":
            print("\nПорівняння книг:")
            print(f"Книга 1: {book1}")
            print(f"Книга 2: {book2}")
            print("Однакові" if book1 == book2 else "Різні")
            print("Книга 1 дешевша" if book1 < book2 else "Книга 2 дешевша")
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")