from flask import Flask, request, jsonify

app_track_workout = Flask(__name__)

@app_track_workout.route('/api/track_workout', methods=['POST', 'GET'])
def track_workout():
    if request.method == 'POST':
        # Post Data
        data = request.get_json()

        username = data['username']
        workout = data['workout']
        time = data['time']
        date = data['date']
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
        <p><input type = "date" name = "date"/></p>
        <p><input type = "submit" name = "submit"/></p>
        </form>'''

if __name__ == '__main__':
    app_track_workout.run(port=5004, debug=True)