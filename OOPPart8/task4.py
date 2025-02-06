class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, genre, year, pages, publisher):
        if title in self.books:
            print(f'Книга "{title}" вже є в колекції.')
        else:
            self.books[title] = {
                "Автор": author,
                "Жанр": genre,
                "Рік випуску": year,
                "Кількість сторінок": pages,
                "Видавництво": publisher
            }
            print(f'Додано книгу: "{title}"')

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f'Книга "{title}" видалена.')
        else:
            print(f'Книги "{title}" немає в колекції.')

    def find_book(self, title):
        return self.books.get(title, f'Книга "{title}" не знайдена.')

    def update_book(self, title, key, new_value):
        if title in self.books:
            if key in self.books[title]:
                self.books[title][key] = new_value
                print(f'Оновлено "{key}" книги "{title}".')
            else:
                print(f'Поле "{key}" не існує.')
        else:
            print(f'Книги "{title}" немає в колекції.')

    def show_all(self):
        if self.books:
            print("Книжкова колекція:")
            for title, details in self.books.items():
                print(f'\nНазва: {title}')
                for key, value in details.items():
                    print(f'  {key}: {value}')
        else:
            print("Колекція порожня.")


collection = BookCollection()

collection.add_book("1984", "Джордж Орвелл", "Антиутопія", 1949, 328, "СЕ")
collection.add_book("Майстер і Маргарита", "Михайло Булгаков", "Роман", 1967, 480, "Радянський письменник")

print(collection.find_book("1984"))

collection.update_book("1984", "Рік випуску", 1950)

collection.remove_book("Майстер і Маргарита")

collection.show_all()
