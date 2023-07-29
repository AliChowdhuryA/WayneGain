from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# URLs of the other microservices
LOGIN_API_URL = "http://localhost:5002/api/login"
REGISTER_API_URL = "http://localhost:5001/api/register"
SEND_EMAIL_API_URL = "http://localhost:5003/api/send_email"
TRACK_WORKOUT_URL = "http://localhost:5004/api/track_workout"
TRACK_WEIGHT_URL = "http://localhost:5005/api/track_weight"
PERSONAL_GOALS_URL = "http://localhost:5006/api/random_goal"
BMI_CALCULATOR_URL = "http://localhost:5007/api/bmi_calc"
GET_STRETCHES_URL = "http://localhost:5008/api/get_stretches"

DAILY_RECIPE_URL = "http://localhost:5010/api/daily_recipe"

DAILY_CALORIES_URL = "http://localhost:5009/api/calorie_input"


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    response = requests.post(LOGIN_API_URL, json=data)
    return jsonify(response.json())

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    response = requests.post(REGISTER_API_URL, json=data)
    return jsonify(response.json())

@app.route('/api/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    response = requests.post(SEND_EMAIL_API_URL, json=data)
    return jsonify(response.json())

@app.route('/api/track_workout', methods=['POST'])
def track_workout():
    data = request.get_json()
    response = requests.post(TRACK_WORKOUT_URL, json=data)
    return jsonify(response.json())

@app.route('/api/track_weight', methods=['POST', 'GET'])
def track_weight():
    data = request.get_json()
    response = requests.post(TRACK_WEIGHT_URL, json=data)
    return jsonify(response.json())

@app.route('/api/random_goal', methods=['GET'])
def random_goal():
    response = requests.get(PERSONAL_GOALS_URL)
    return jsonify(response.json()), response.status_code

@app.route('/api/bmi_calc',methods=['GET','POST'])
def bmi_calc():
    if request.method == 'POST':
        data = request.get_json()
        response = requests.post(BMI_CALCULATOR_URL, json=data)
        return jsonify(response.json()), response.status_code

@app.route('/api/get_stretches', methods=['POST', 'GET'])
def get_stretches():
    data = request.get_json()
    response = requests.post(GET_STRETCHES_URL, json=data)
    return jsonify(response.json())

@app.route('/api/calorie_input', methods=['POST'])
def calorie_input():
    data = request.get_json()
    response = requests.post(DAILY_CALORIES_URL, json=data)
    return jsonify(response.json())

@app.route('/api/daily_recipe', methods=['POST', 'GET'])
def daily_recipe():
    response = requests.get(DAILY_RECIPE_URL)
    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(port=5000, debug=True)