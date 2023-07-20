from flask import Flask, request, jsonify

app_register = Flask(__name__)

@app_register.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    # Extract user registration details from the request data
    username = data['username']
    password = data['password']
    # Perform validation and store user details in the database

    return jsonify({'message': 'User registered successfully'})

if __name__ == '__main__':
    app_register.run(port=5001, debug=True)