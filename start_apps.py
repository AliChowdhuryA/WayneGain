import subprocess

# List of apps to start with their respective port numbers
apps = [
    ("apigateway.py", 5000),
    ("register.py", 5001),
    ("login.py", 5002),
    ("send_email.py", 5003),
    ("workouts.py", 5004),
    ("weight_tracker.py", 5005),
    ("personal_goals.py", 5006),
    ("bmi_c.py", 5007),
    ("get_stretches.py", 5008),
    ("daily_calories.py", 5009),
    ("dailyRec.py", 5010),
    ("databaseAPI.py", 5011),
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
