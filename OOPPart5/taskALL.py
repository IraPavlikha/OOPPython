from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://swapi.dev/api/"

@app.route('/')
def index():
    return render_template('index.html')

# Завдання 1
# Використовуючи API, відобразіть назви усіх фільмів серії.
# Виведіть інформацію про певний фільм, на який виконується клік.
@app.route('/films', methods=['GET'])
def get_films():
    response = requests.get(f"{BASE_URL}films/")
    if response.status_code == 200:
        return jsonify(response.json()["results"])
    return jsonify({"error": "Не вдалося отримати фільми"}), 500

# Деталі про фільм
@app.route('/films/<int:film_id>', methods=['GET'])
def get_film_details(film_id):
    response = requests.get(f"{BASE_URL}films/{film_id}/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Не вдалося отримати інформацію про фільм"}), 500

# Завдання 2
# Використовуючи API, відобразіть імена головних героїв
# серії. Виведіть інформацію про певного героя, на який виконується клік.
@app.route('/people', methods=['GET'])
def get_people():
    response = requests.get(f"{BASE_URL}people/")
    if response.status_code == 200:
        return jsonify(response.json()["results"])
    return jsonify({"error": "Не вдалося отримати персонажів"}), 500

# Деталі про персонажа
@app.route('/people/<int:person_id>', methods=['GET'])
def get_person_details(person_id):
    response = requests.get(f"{BASE_URL}people/{person_id}/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Не вдалося отримати інформацію про персонажа"}), 500

# Завдання 3
# Використовуючи API, відобразіть назви планет. Виведіть
# інформацію про певну планету, на яку виконується клік.
@app.route('/planets', methods=['GET'])
def get_planets():
    response = requests.get(f"{BASE_URL}planets/")
    if response.status_code == 200:
        return jsonify(response.json()["results"])
    return jsonify({"error": "Не вдалося отримати планети"}), 500

# Деталі про планету
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_details(planet_id):
    response = requests.get(f"{BASE_URL}planets/{planet_id}/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Не вдалося отримати інформацію про планету"}), 500

# Завдання 4
# Використовуючи API, відобразіть назви кораблів. Виведіть
# інформацію про певний корабель, на який виконується клік.
@app.route('/starships', methods=['GET'])
def get_starships():
    response = requests.get(f"{BASE_URL}starships/")
    if response.status_code == 200:
        return jsonify(response.json()["results"])
    return jsonify({"error": "Не вдалося отримати кораблі"}), 500

# Деталі про корабель
@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship_details(starship_id):
    response = requests.get(f"{BASE_URL}starships/{starship_id}/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Не вдалося отримати інформацію про корабель"}), 500

if __name__ == '__main__':
    app.run(debug=True)
