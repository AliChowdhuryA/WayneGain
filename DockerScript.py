import os

#only tested on windows

#create docker images and run them

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

os.system("docker run -d -p 5000:5000/tcp --name apigateway apigateway")
os.system("docker run -d -p 5001:5001/tcp --name register register")
os.system("docker run -d -p 5002:5002/tcp --name login login")
os.system("docker run -d -p 5003:5003/tcp --name email send_email")
os.system("docker run -d -p 5004:5004/tcp --name track_workout track_workout")
os.system("docker run -d -p 5005:5005/tcp --name track_weight track_weight")
os.system("docker run -d -p 5006:5006/tcp --name goals goals")
os.system("docker run -d -p 5007:5007/tcp --name bmi_cal bmi_cal")
os.system("docker run -d -p 5008:5008/tcp --name get_stretch get_stretch")
os.system("docker run -d -p 5009:5009/tcp --name daily_calories daily_calories")
os.system("docker run -d -p 5010:5010/tcp --name daily_rec daily_rec")
os.system("docker run -d -p 5011:5011/tcp --name database database")