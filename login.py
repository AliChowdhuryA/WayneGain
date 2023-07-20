from flask import Flask, request, jsonify

app_login = Flask(__name__)

@app_login.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # Extract user login credentials from the request data
    username = data['username']
    password = data['password']
    # Perform validation and authenticate user against stored credentials

    return jsonify({'message': 'User logged in successfully'})

if __name__ == '__main__':
    app_login.run(port=5002, debug=True)