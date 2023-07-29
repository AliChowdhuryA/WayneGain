from flask import Flask, redirect, url_for, request
from datetime import date
app = Flask(__name__)

# tested on postman using localhost:5009/api/daily_calories
# will return a json of calories and today date
# if fail will return a string of the error
@app.route('/api/daily_calories',methods = ['POST'])
def daily_calories():
    if request.method == 'POST':
        inputData = request.get_json()
        data = inputData['cal']
        if(data is None):
            return {"Error":"No data has been passed"}
        today = date.today()
        return {"date" : today, "calories" : data}
    return {"Error": "Not POST"}

if __name__ == '__main__':
   app.run(port=5009,debug=True)
