from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def generate_random_number():
    number = random.randint(0, 100)
    return jsonify({"випадкове_число": number})

@app.route('/random/range', methods=['GET'])
def generate_random_number_in_range():
    try:
        min_value = int(request.args.get('min', 0))
        max_value = int(request.args.get('max', 100))
        if min_value > max_value:
            return jsonify({"помилка": "Мінімальне значення не може бути більшим за максимальне."}), 400
        number = random.randint(min_value, max_value)
        return jsonify({"випадкове_число": number})
    except ValueError:
        return jsonify({"помилка": "Невірний ввід. Будь ласка, введіть цілі числа для мінімального та максимального значення."}), 400

@app.route('/random/set', methods=['GET'])
def generate_random_numbers_set():
    try:
        count = int(request.args.get('count', 1))
        min_value = int(request.args.get('min', 0))
        max_value = int(request.args.get('max', 100))
        if count < 1:
            return jsonify({"помилка": "Кількість чисел має бути хоча б 1."}), 400
        if min_value > max_value:
            return jsonify({"помилка": "Мінімальне значення не може бути більшим за максимальне."}), 400
        numbers = [random.randint(min_value, max_value) for _ in range(count)]
        return jsonify({"набір_випадкових_чисел": numbers})
    except ValueError:
        return jsonify({"помилка": "Невірний ввід. Будь ласка, введіть цілі числа для параметрів 'count', 'min', та 'max'."}), 400

if __name__ == '__main__':
    app.run(debug=True)