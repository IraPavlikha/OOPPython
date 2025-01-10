from flask import Flask, jsonify
import random
app = Flask(__name__)

predictions = [
    "Сьогодні вас чекає щось приємне!",
    "Ваша наполегливість скоро окупиться.",
    "Будьте уважні до дрібниць, вони можуть змінити ваш день.",
    "Нові можливості вже поруч, не проґавте їх.",
    "Ваша усмішка сьогодні допоможе вам знайти нових друзів.",
    "Варто приділити час собі, це допоможе знайти гармонію.",
    "Сміливо беріться за нові виклики!",
    "Сьогодні - чудовий день для нових починань.",
]

@app.route('/api/fortune', methods=['GET'])
def get_fortune():
    prediction = random.choice(predictions)
    return jsonify({"fortune": prediction})

if __name__ == '__main__':
    app.run(debug=True)
