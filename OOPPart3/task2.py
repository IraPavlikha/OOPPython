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
        return (f"Назва рецепту: {self.name}\nАвтор: {self.author}\nТип рецепту: {self.recipe_type}\n"
                f"Опис: {self.description}\nПосилання на відео: {self.video_link}\n"
                f"Інгредієнти: {', '.join(self.ingredients)}\nКухня: {self.cuisine}")

class RecipeView:
    @staticmethod
    def display_recipe_details(recipe):
        print("\nДеталі рецепту:")
        print(recipe)

    @staticmethod
    def display_all_recipes(recipes):
        print("\nУсі рецепти:")
        for recipe in recipes:
            print(recipe)

class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        new_recipe = Recipe(name, author, recipe_type, description, video_link, ingredients, cuisine)
        self.recipes.append(new_recipe)
        return new_recipe

    def get_recipe(self, index):
        if 0 <= index < len(self.recipes):
            return self.recipes[index]
        else:
            raise IndexError("Рецепт не знайдено.")

    def get_all_recipes(self):
        return self.recipes

if __name__ == "__main__":
    controller = RecipeController()
    view = RecipeView()
    recipe1 = controller.add_recipe(
        "Борщ", "Ольга", "Перша страва", "Традиційна українська страва з буряком.",
        "https://example.com/borshch", ["буряк", "картопля", "морква", "капуста", "м'ясо"], "Українська")

    recipe2 = controller.add_recipe(
        "Паста Карбонара", "Джованні", "Друга страва", "Італійська паста з беконом та яйцем.",
        "https://example.com/carbonara", ["паста", "бекон", "яйця", "сир Пармезан", "вершки"], "Італійська")

    view.display_recipe_details(recipe1)
    all_recipes = controller.get_all_recipes()
    view.display_all_recipes(all_recipes)