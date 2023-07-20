from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URLs of the other microservices
LOGIN_API_URL = "http://localhost:5002/api/login"
REGISTER_API_URL = "http://localhost:5001/api/register"
SEND_EMAIL_API_URL = "http://localhost:5003/api/send_email"

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)