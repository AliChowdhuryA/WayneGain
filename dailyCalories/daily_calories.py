from flask import Flask, redirect, url_for, request, jsonify
from datetime import date
app = Flask(__name__)

# tested on postman using localhost:5000/calorie_input
# will return a json of calories and today date
# if fail will return a string of the error
@app.route('/api/daily_calories',methods = ['POST'])
def daily_calories():
    if request.method == 'POST':
        #data = request.args.get("cal")
        data = request.get_json()
        if(data is None):
            return {"Error":"No data has been passed"}
        today = date.today()
        user = data['user']
        caloric_intake = data['caloric_intake']
        return jsonify({"user": user, "date" : today, "calories" : caloric_intake})
    #return "Error"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5009,debug=True)
