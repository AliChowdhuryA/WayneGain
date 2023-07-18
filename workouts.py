from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/track_workout', methods=['POST', 'GET'])
def track_workout():
    if request.method == 'POST':
        # Post Data
        username = request.form['username']
        workout = request.form['workout']
        time = request.form['time']
        date = request.form['date']
        submission = {
            'username': username,
            'workout': workout,
            'time': time,
            'date': date
        }
        return jsonify(submission)
    else:
        # Display Form to input data
        return '''<form method = "post">
        <p>Enter Username:</p>
        <p><input type = "text" name = "username"/></p>
        <p>Enter Workout:</p>
        <p><input type = "text" name = "workout"/></p>
        <p>Enter Time Spent (Hours:Minutes):</p>
        <p><input type = "text" name = "time"/></p>
        <p>Enter Date (MM/DD/YYYY):</p>
        <p><input type = "text" name = "date"/></p>
        <p><input type = "submit" name = "submit"/></p>
        </form>'''

if __name__ == '__main__':
    app.run(debug=True)