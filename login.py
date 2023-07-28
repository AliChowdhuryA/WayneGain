from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == "GET":
        #when using the GET method in Postman, program will return this
        return jsonify({"response": "Get Request Called"})
    elif request.method == "POST":
        data = request.get_json()
        # Extract user login credentials from the request data
        username = data['username']
        password = data['password']
        # Perform validation and authenticate user against stored credentials

        return jsonify({'message': 'User logged in successfully'})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
