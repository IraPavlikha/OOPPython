class EnglishFrenchDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, english, french):
        self.dictionary[english] = french
        print(f'Додано: {english} → {french}')

    def remove_word(self, english):
        if english in self.dictionary:
            del self.dictionary[english]
            print(f'Видалено: {english}')
        else:
            print(f'Слова "{english}" немає в словнику.')

    def find_word(self, english):
        return self.dictionary.get(english, f'Слово "{english}" не знайдено.')

    def update_word(self, english, new_french):
        if english in self.dictionary:
            self.dictionary[english] = new_french
            print(f'Оновлено: {english} → {new_french}')
        else:
            print(f'Слова "{english}" немає в словнику.')

    def show_all(self):
        if self.dictionary:
            print("Англо-французький словник:")
            for eng, fr in self.dictionary.items():
                print(f'{eng} → {fr}')
        else:
            print("Словник порожній.")


dictionary = EnglishFrenchDictionary()

dictionary.add_word("hello", "bonjour")
dictionary.add_word("apple", "pomme")

print(dictionary.find_word("apple"))  # pomme

dictionary.update_word("apple", "la pomme")

dictionary.remove_word("hello")

dictionary.show_all()