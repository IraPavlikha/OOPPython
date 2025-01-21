class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return (f"Назва рецепту: {self.name}, Автор: {self.author}, Тип: {self.recipe_type}, "
                f"Опис: {self.description}, Відео: {self.video_link}, "
                f"Інгредієнти: {', '.join(self.ingredients)}, Кухня: {self.cuisine}")

class RecipeView:
    @staticmethod
    def display_recipe_details(recipe):
        print("\nДеталі рецепту:")
        print(recipe)

    @staticmethod
    def display_all_recipes(recipes):
        print("\nСписок усіх доступних рецептів:")
        for index, recipe in enumerate(recipes, start=1):
            print(f"{index}. {recipe}")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_input(prompt):
        return input(prompt)

class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self):
        name = RecipeView.get_input("Введіть назву рецепту: ")
        author = RecipeView.get_input("Введіть автора рецепту: ")
        recipe_type = RecipeView.get_input("Введіть тип рецепту (перші страви, другі страви тощо): ")
        description = RecipeView.get_input("Введіть опис рецепту: ")
        video_link = RecipeView.get_input("Введіть посилання на відео з рецептом: ")
        ingredients = RecipeView.get_input("Введіть інгредієнти (розділіть комами): ").split(',')
        cuisine = RecipeView.get_input("Введіть назву кухні (італійська, французька тощо): ")
        new_recipe = Recipe(name, author, recipe_type, description, video_link, [ingredient.strip() for ingredient in ingredients], cuisine)
        self.recipes.append(new_recipe)
        RecipeView.display_message("Новий рецепт успішно додано!")
    def get_recipe_details(self):
        try:
            index = int(RecipeView.get_input("Введіть номер рецепту для перегляду: ")) - 1
            if 0 <= index < len(self.recipes):
                RecipeView.display_recipe_details(self.recipes[index])
            else:
                RecipeView.display_message("Помилка: Рецепт не знайдено.")
        except ValueError:
            RecipeView.display_message("Помилка: Введіть коректний номер.")
    def show_all_recipes(self):
        if self.recipes:
            RecipeView.display_all_recipes(self.recipes)
        else:
            RecipeView.display_message("Список рецептів порожній.")
if __name__ == "__main__":
    controller = RecipeController()
    while True:
        print("\nМеню:")
        print("1. Додати новий рецепт")
        print("2. Показати всі рецепти")
        print("3. Переглянути деталі конкретного рецепту")
        print("4. Вийти")
        choice = RecipeView.get_input("Виберіть опцію (1-4): ")
        if choice == "1":
            controller.add_recipe()
        elif choice == "2":
            controller.show_all_recipes()
        elif choice == "3":
            controller.get_recipe_details()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")