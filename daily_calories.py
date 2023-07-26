from flask import Flask, redirect, url_for, request
from datetime import date
app = Flask(__name__)

# tested on postman using localhost:5000/daily_calories
# will return a json of calories and today date
# if fail will return a string of the error
@app.route('/daily_calories',methods = ['POST'])
def daily_calories():
    if request.method == 'POST':
        data = request.args.get("cal")
        if(data is None):
            return "No data has been passed"
        today = date.today()
        return {"date" : today, "calories" : data}
    return "Error"

if __name__ == '__main__':
   app.run(debug=True)
