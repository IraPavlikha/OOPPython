from flask import Flask, jsonify
import random

app = Flask(__name__)

poems = [
    {"title": "Любов і ніжність", "author": "Тарас Шевченко", "theme": "любов", "text": "Кохайтеся, чорнобриві, та не з москалями..."},
    {"title": "Моя муза", "author": "Леся Українка", "theme": "творчість", "text": "Як я умру, на світі запалає..."},
    {"title": "Життя і смерть", "author": "Іван Франко", "theme": "життя", "text": "Життя – це боротьба, і не на жарт..."}
]

def get_random_poem():
    return random.choice(poems)

def get_random_poem_by_author(author):
    author_poems = [poem for poem in poems if poem["author"] == author]
    return random.choice(author_poems) if author_poems else None

def get_random_poem_by_theme(theme):
    theme_poems = [poem for poem in poems if poem["theme"] == theme]
    return random.choice(theme_poems) if theme_poems else None

@app.route("/random_poem", methods=["GET"])
def random_poem():
    return jsonify(get_random_poem())

@app.route("/random_poem/author/<author>", methods=["GET"])
def random_poem_author(author):
    poem = get_random_poem_by_author(author)
    return jsonify(poem) if poem else ("Author not found", 404)

@app.route("/random_poem/theme/<theme>", methods=["GET"])
def random_poem_theme(theme):
    poem = get_random_poem_by_theme(theme)
    return jsonify(poem) if poem else ("Theme not found", 404)

@app.route("/authors", methods=["GET"])
def list_authors():
    authors = list(set(poem["author"] for poem in poems))
    return jsonify(authors)

@app.route("/themes", methods=["GET"])
def list_themes():
    themes = list(set(poem["theme"] for poem in poems))
    return jsonify(themes)

@app.route("/poems/author/<author>", methods=["GET"])
def list_poems_by_author(author):
    titles = [poem["title"] for poem in poems if poem["author"] == author]
    return jsonify(titles) if titles else ("Author not found", 404)

@app.route("/poems/theme/<theme>", methods=["GET"])
def list_poems_by_theme(theme):
    titles = [poem["title"] for poem in poems if poem["theme"] == theme]
    return jsonify(titles) if titles else ("Theme not found", 404)

if __name__ == "__main__":
    app.run(debug=True)