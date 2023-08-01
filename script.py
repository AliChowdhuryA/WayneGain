import os

os.system("docker build --tag database ./database/")
os.system("docker build --tag apigateway ./apigateway/")
os.system("docker build --tag register ./register/")
os.system("docker build --tag login ./login/")
os.system("docker build --tag bmi_cal ./bmiCalc/")
os.system("docker build --tag daily_calories ./dailyCalories/")
os.system("docker build --tag daily_rec ./dailyRec/")
os.system("docker build --tag get_stretch ./getStretch/")
os.system("docker build --tag goals ./goals/")
os.system("docker build --tag send_email ./sendEmail/")
os.system("docker build --tag track_weight ./trackWeight/")
os.system("docker build --tag track_workout ./trackWorkout/")
