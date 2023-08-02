from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# URLs of the other microservices
REGISTER_API_URL = "http://host.docker.internal:5001/api/register"
LOGIN_API_URL = "http://host.docker.internal:5002/api/login"
SEND_EMAIL_API_URL = "http://host.docker.internal:5003/api/send_email"
TRACK_WORKOUT_URL = "http://host.docker.internal:5004/api/track_workout"
TRACK_WEIGHT_URL = "http://host.docker.internal:5005/api/track_weight"
PERSONAL_GOALS_URL = "http://host.docker.internal:5006/api/random_goal"
BMI_CALCULATOR_URL = "http://host.docker.internal:5007/api/bmi_calc"
GET_STRETCHES_URL = "http://host.docker.internal:5008/api/get_stretches"
DAILY_CALORIES_URL = "http://host.docker.internal:5009/api/daily_calories"
DAILY_RECIPE_URL = "http://host.docker.internal:5010/api/daily_recipe"
DATABASE_URL= "http://host.docker.internal:5011/api/database"


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

@app.route('/api/daily_calories', methods=['POST'])
def calorie_input():
    data = request.get_json()
    response = requests.post(DAILY_CALORIES_URL, json=data)
    return jsonify(response.json())

@app.route('/api/daily_recipe', methods=['POST', 'GET'])
def daily_recipe():
    response = requests.get(DAILY_RECIPE_URL)
    return jsonify(response.json()), response.status_code

# EX: http://localhost:5000/api/database/login/?username=test&password=1234
@app.route('/api/database/login/', methods=['GET'])
def database_login():

    username = request.args.get('username')
    password = request.args.get('password')
    
    response = requests.get(f"{DATABASE_URL}/login/{username}/{password}")
    
    return jsonify(response.json()), response.status_code
# EX: http://localhost:5000/api/database/register/?username=test&password=1234
@app.route('/api/database/register/', methods=['GET'])
def database_register():

    username = request.args.get('username')
    password = request.args.get('password')
    
    response = requests.get(f"{DATABASE_URL}/register/{username}/{password}")
    
    return jsonify(response.json()), response.status_code

@app.route('/api/database/daily_calories', methods=['POST'])
def database_daily_calories():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/daily_calories", json=data)
    return jsonify(response.json())

@app.route('/api/database/print_daily_calories', methods=['POST'])
def database_print_daily_calories():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/print_daily_calories", json=data)
    return jsonify(response.json())

@app.route('/api/database/track_weight', methods=['POST'])
def database_track_weight():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/track_weight", json=data)
    return jsonify(response.json())

@app.route('/api/database/print_track_weight', methods=['POST'])
def database_print_track_weight():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/print_track_weight", json=data)
    return jsonify(response.json())

@app.route('/api/database/track_workout', methods=['POST'])
def database_track_workout():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/track_workout", json=data)
    return jsonify(response.json())

@app.route('/api/database/print_track_workout', methods=['POST'])
def database_print_track_workout():
    data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/print_track_workout", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5015, debug=True)
