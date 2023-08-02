from flask import Flask, render_template, request, redirect, url_for, session, g
import requests, json

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Change this to a strong secret key

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        url = "http://host.docker.internal:5015/api/login"

        return_url = requests.post(url, json={"username": username, "password": password})
        json_url = json.loads(return_url.text)

        if "Failed" in json_url.keys():
            error = "Invalid username or password. Please try again."
            return render_template('login.html', error=error)

        if "User" in json_url.keys():
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        url = "http://host.docker.internal:5015/api/register"
        return_url = requests.post(url, json={"username": username, "password": password})
        json_url = json.loads(return_url.text)

        if "Failed" in json_url.keys():
            error = "Username Taken. Please try again."
            return render_template('register.html', error=error)

        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/daily_calories', methods=['GET', 'POST'])
def daily_calories():
    if request.method == 'POST' and 'username' in session:
        calories = request.form['calories']
        if calories.isdigit():
            url = "http://host.docker.internal:5015/api/daily_calories"
            return_url = requests.post(url, json={"user": session["username"], "caloric_intake": calories})
            json_url = json.loads(return_url.text)
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/daily_calories"
            return_url = requests.post(database_url, json=json_url)
            json_url = json.loads(return_url.text)
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/print_daily_calories"
            history_url = requests.post(database_url, json={"username": session["username"]})
            history_data = json.loads(history_url.text)
            print(json_url)

            print(f"Daily calories tracked for user {session['username']}: {calories}")
            return render_template('daily_calories.html', calories=calories, history_data=history_data)
        print("failed")
    return redirect(url_for('dashboard'))

@app.route('/track_weight', methods=['GET', 'POST'])
def track_weight():
    if request.method == 'POST' and 'username' in session:
        weight = request.form['weight']
        if weight.isdigit():
            url = "http://host.docker.internal:5015/api/track_weight"
            return_url = requests.post(url, json={"username": session["username"], "weight": weight})
            json_url = json.loads(return_url.text)
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/track_weight"
            return_url = requests.post(database_url, json=json_url)
            json_url = json.loads(return_url.text)
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/print_track_weight"
            history_url = requests.post(database_url, json={"username": session["username"]})
            history_data = json.loads(history_url.text)
            print(json_url)

            print(f"Weight tracked for user {session['username']}: {weight}")
            return render_template('track_weight.html', weight=weight, history_data=history_data)
        print("failed")
    return redirect(url_for('dashboard'))

@app.route('/track_workout', methods=['GET', 'POST'])
def track_workout():
    if request.method == 'POST' and 'username' in session:
        workout = request.form['workout']
        time = request.form['time']
        date = request.form['date']
        if workout != None and time != None and date != None:
            url = "http://host.docker.internal:5015/api/track_workout"
            return_url = requests.post(url, json={"username": session["username"], "workout": workout, "time":time, "date":date})
            json_url = json.loads(return_url.text)
            json_url["date"] = json_url["date"]+ " "+ json_url["time"]
            json_url.pop("time")
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/track_workout"
            return_url = requests.post(database_url, json=json_url)
            json_url = json.loads(return_url.text)
            print(json_url)
            database_url = "http://host.docker.internal:5015/api/database/print_track_workout"
            history_url = requests.post(database_url, json={"username": session["username"]})
            history_data = json.loads(history_url.text)
            print(json_url)

            print(f"Workout tracked for user {session['username']}: {workout} at {time} on {date}")
            return render_template('track_workout.html', workout=workout, history_data=history_data)

        print("failed")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5020)
