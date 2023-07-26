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
        data = {
            "weight": request.form['weight'],
            "hFeet": request.form['hFeet'],
            "hInch": request.form['hInch']
        }
        response = requests.post(BMI_CALCULATOR_URL, data=data)
        return jsonify(response.json()), response.status_code

    else:
        input_template = """
            <h1>BMI Calculator</h1>
                <br>
                <h3> Less Than 18.5 Underweight </h3>
                <h3> 18.5 to 24.9 Normal Weight </h3>
                <h3> 25 to 29.9 Overweight </h3>
                <h3> More Than 30 Underweight </h3>
                </br>
            <form action="/api/bmi_calc" method="post">
                <label for="weight">Weight(lb)   </label>
                <input type="text" name="weight" id="weight" required>
                <br>
                <label for="hFeet">Height (ft)    </label>
                <input type="text" name="hFeet" id="hFeet" required>
                <br>
                <label for="hInch">Height (in)    </label>
                <input type="text" name="hInch" id="hInch" required>
                </br>
                <input type="submit" value="Submit">
            </form>
        """
        
        return render_template_string(input_template)

@app.route('/api/get_stretches', methods=['POST', 'GET'])
def get_stretches():
    data = request.get_json()
    response = requests.post(GET_STRETCHES_URL, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)