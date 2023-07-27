# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python files for each app to the container
COPY apigateway.py apigateway.py
COPY databaseAPI.py databaseAPI.py
COPY send_email.py send_email.py
COPY get_stretches.py get_stretches.py
COPY dailyRec.py dailyRec.py
COPY bmi_c.py bmi_c.py
COPY daily_calories.py daily_calories.py
COPY personal_goals.py personal_goals.py
COPY workouts.py workouts.py
COPY weight_tracker.py weight_tracker.py
COPY login.py login.py
# Install the required dependencies for each app
RUN pip install --no-cache-dir Flask

# Expose port 5000 for all apps
EXPOSE 5000

# Start each app on a different port
CMD ["python", "start_apps.py"]