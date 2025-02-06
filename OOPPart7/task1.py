from flask import Flask, jsonify
import random

app = Flask(__name__)

predictions = [
    "Вам щастить у коханні.",
    "Не бійтеся нових починань.",
    "Ваші зусилля будуть винагороджені.",
    "Сьогодні ваш день!",
    "Вас чекає приємна несподіванка.",
    "Довіртеся своїй інтуїції.",
    "Новий проект принесе успіх.",
    "Ви знайдете те, що шукаєте.",
    "Ваша наполегливість буде винагороджена.",
    "Сьогоднішній день принесе вам радість."
]

@app.route('/api/prediction', methods=['GET'])
def get_prediction():
    prediction = random.choice(predictions)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)