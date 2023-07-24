from flask import Flask, jsonify
import random

app = Flask(__name__)

daily_goals = [
    "Read for 30 minutes",
    "Drink 2 liters of water",
    "Walk 10,000 steps",
<<<<<<< HEAD
    "Learn something new",
    "Get 2 workouts done in a day",
    "Eat Healthy 6/7 days of a week",
    "Try to read 5 pages a day",
    "Keep my room clean!"
=======
    "Spend quality time with family",
    "Learn something new",
    "Get 2 workouts done in a day",
    "Eat Healthy 6/7 days of a week",
    ""
>>>>>>> 6494f5a (Added goals)

]

@app.route('/random_goal', methods=['GET'])
def get_random_goal():
    return jsonify({"goal": random.choice(daily_goals)}), 200

if __name__ == '__main__':
    app.run(debug=True)
