import subprocess

# List of apps to start with their respective port numbers
apps = [
    ("apigateway.py", 5000),
    ("databaseAPI.py", 5001),
    ("send_email.py", 5002),
    ("get_stretches.py", 5003),
    ("dailyRec.py", 5004),
    ("bmi_c.py", 5005),
    ("daily_calories.py", 5006),
    ("personal_goals.py", 5007),
    ("workouts.py", 5008),
    ("weight_tracker.py", 5009),
    ("login.py", 5010),
]

# Start each app in the background
processes = []
for app, port in apps:
    cmd = ["python", app, "--port", str(port)]
    process = subprocess.Popen(cmd)
    processes.append(process)

# Wait for all background processes to finish
for process in processes:
    process.wait()
