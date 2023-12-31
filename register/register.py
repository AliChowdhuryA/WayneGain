from flask import Flask, request, jsonify
import requests

app_register = Flask(__name__)

@app_register.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    # Extract user registration details from the request data
    username = data['username']
    password = data['password']
    # Perform validation and store user details in the database
    url = f"http://host.docker.internal:5015/api/database/register/?username={username}&password={password}"
    return requests.get(url).text

    #return jsonify({'message': 'User registered successfully'})

if __name__ == '__main__':
    app_register.run(host='0.0.0.0', port=5001, debug=True)
