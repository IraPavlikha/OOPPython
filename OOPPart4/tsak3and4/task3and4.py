from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Дані для сервісу
poems = [
    {"title": "Мій коханий сад", "author": "Леся Українка", "theme": "любов", "text": "Коханий сад, ти радість моя..."},
    {"title": "Життя і боротьба", "author": "Іван Франко", "theme": "життя", "text": "Життя - це постійна боротьба..."},
    {"title": "Мрії творчості", "author": "Тарас Шевченко", "theme": "творчість", "text": "Творчість в моїх мріях вічна..."},
    {"title": "Кохання - дарунок", "author": "Ліна Костенко", "theme": "любов", "text": "Кохання - це дарунок з небес..."}
]

# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')

# Випадковий вірш
@app.route('/api/random-poem', methods=['GET'])
def get_random_poem():
    poem = random.choice(poems)
    return jsonify(poem)

# Випадковий вірш автора
@app.route('/api/random-poem-by-author', methods=['GET'])
def get_random_poem_by_author():
    author = request.args.get('author')
    author_poems = [poem for poem in poems if poem['author'] == author]
    if author_poems:
        return jsonify(random.choice(author_poems))
    return jsonify({"error": "Автор не знайдений"}), 404

# Випадковий вірш за тематикою
@app.route('/api/random-poem-by-theme', methods=['GET'])
def get_random_poem_by_theme():
    theme = request.args.get('theme')
    theme_poems = [poem for poem in poems if poem['theme'] == theme]
    if theme_poems:
        return jsonify(random.choice(theme_poems))
    return jsonify({"error": "Тема не знайдена"}), 404

# Назви усіх віршів автора
@app.route('/api/poems-by-author', methods=['GET'])
def get_poems_by_author():
    author = request.args.get('author')
    author_poems = [poem['title'] for poem in poems if poem['author'] == author]
    if author_poems:
        return jsonify(author_poems)
    return jsonify({"error": "Автор не знайдений"}), 404

# Список усіх авторів
@app.route('/api/authors', methods=['GET'])
def get_authors():
    authors = list(set(poem['author'] for poem in poems))
    return jsonify(authors)

# Список усіх тематик
@app.route('/api/themes', methods=['GET'])
def get_themes():
    themes = list(set(poem['theme'] for poem in poems))
    return jsonify(themes)

# Назви усіх віршів за вказаною тематикою
@app.route('/api/poems-by-theme', methods=['GET'])
def get_poems_by_theme():
    theme = request.args.get('theme')
    theme_poems = [poem['title'] for poem in poems if poem['theme'] == theme]
    if theme_poems:
        return jsonify(theme_poems)
    return jsonify({"error": "Тема не знайдена"}), 404

if __name__ == '__main__':
    print("\u0412\u0435\u0431\u0441\u0435\u0440\u0432\u0456\u0441 \u043f\u043e\u0447\u0430\u0442\u043e. \u0412\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u043e\u0432\u0443\u0439\u0442\u0435 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0456 API-м\u0430\u0440\u0448\u0440\u04430449\u0442\u0438.")
    app.run(debug=True)
