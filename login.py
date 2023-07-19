from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/register', methods=['GET','POST'])
def register():
    if request.method == "GET":
        #when using the GET method in Postman, program will return this
        return jsonify({"response": "Get Request Called"})
    elif request.method == "POST":
        #When using POST method, program will take details and register them in the database
        data = request.json
        # Extract user registration details from the request data
        username = data['username']
        password = data['password']
        # Perform validation and store user details in the database

        return jsonify({'message': 'User registered successfully'})


@app.route('/api/login', methods=['GET', 'POST'])
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
    app.run(debug=True)
