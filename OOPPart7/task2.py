from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_number():
    random_number = random.randint(0, 100)
    return jsonify({"random_number": random_number})

@app.route('/random/range', methods=['GET'])
def get_random_number_in_range():
    min_value = int(request.args.get('min', 0))
    max_value = int(request.args.get('max', 100))
    random_number = random.randint(min_value, max_value)
    return jsonify({"random_number": random_number})

@app.route('/random/list', methods=['GET'])
def get_random_number_list():
    count = int(request.args.get('count', 5))
    min_value = int(request.args.get('min', 0))
    max_value = int(request.args.get('max', 100))
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]
    return jsonify({"random_numbers": random_numbers})

if __name__ == '__main__':
    app.run(debug=True)