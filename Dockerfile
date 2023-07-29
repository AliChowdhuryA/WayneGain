# Use the official Python image as the base image
FROM python:3.9

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Set the working directory inside the container
WORKDIR /app

# Install the required dependencies for all apps (Flask and other dependencies)
RUN pip install --no-cache-dir -r requirements.txt

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Create a new non-root user
RUN groupadd -r myuser && useradd -r -g myuser myuser

# Copy all the Python files for each app to the /app directory inside the container
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
COPY register.py register.py

# Copy the Supervisor configuration file
COPY supervisord.conf /etc/supervisord.conf

# Expose port 5000 for all apps
EXPOSE 5000-5010

# Start Supervisor to manage the processes
CMD ["/usr/bin/supervisord"]
