from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        # Extract user login credentials from the request data
        username = data['username']
        password = data['password']
        # Perform validation and authenticate user against stored credentials
        url = f"http://localhost:5000/api/database/login/?username={username}&password={password}"
        return (requests.get(url)).text

        #return jsonify({'message': 'User logged in successfully'})
    return {"Error": "No Post"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
