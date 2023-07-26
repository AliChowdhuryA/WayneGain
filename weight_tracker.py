from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/api/track_weight', methods=['POST', 'GET'])
def track_workout():
    if request.method == 'POST':
        # Post Data
        username = request.form['username']
        weight = request.form['weight']
        today = date.today().strftime('%Y-%m-%d')
        submission = {
            'username': username,
            'weight': weight,
            'date': today
        }
        return jsonify(submission)
    else:
        # Display Form to input data
        return '''<form method = "post">
        <p>Enter Username:</p>
        <p><input type = "text" name = "username"/></p>
        <p>Enter Weight:</p>
        <p><input type = "number" name = "weight"/></p>
        <p><input type = "submit" name = "submit"/></p>
        </form>'''

if __name__ == '__main__':
    app.run(debug=True)