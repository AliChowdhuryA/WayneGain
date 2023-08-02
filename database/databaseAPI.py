from flask import Flask, request
from flask_restful import Api, Resource
import database as db

app = Flask(__name__)
api = Api(app)


class register(Resource):
    def get(self, username, password):
        if db.checkUsernameIsAvailable(username):
            db.addAccount(username, password)
            return {"User": f"{username} added"}
        return {"Failed":f"Failed adding {username}"}


class login(Resource):
    def get(self, username, password):
        if db.checkAccount(username, password):
            return {"User": f"{username} is now logged in"}
        return {"Failed": "Login Failed"}


class DailyCalories(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"Error": "Invalid JSON data"}, 400

        username = data.get("username")
        calories = data.get("calories")
        date = data.get("date")

        if not all([username, calories, date]):
            return {"Error": "Incomplete data. Please provide username, calories, and date."}, 400

        db.addDailyCalories(username, calories, date)

        return {
            "username": username,
            "calories": calories,
            "date": date
        }

class PrintDailyCalories(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"Error": "Invalid JSON data"}, 400

        username = data.get("username")

        if not all([username]):
            return {"Error": "Incomplete data. Please provide username."}, 400
        
        return db.searchDailyCalories(username)

class TrackWeight(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"Error": "Invalid JSON data"}, 400

        username = data.get("username")
        weight = data.get("weight")
        date = data.get("date")

        if not all([username, weight, date]):
            return {"Error": "Incomplete data. Please provide username, weight, and date."}, 400

        db.addTrackWeight(username, weight, date)

        return {
            "username": username,
            "weight": weight,
            "date": date
        }

class PrintTrackWeight(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"Error": "Invalid JSON data"}, 400

        username = data.get("username")

        if not all([username]):
            return {"Error": "Incomplete data. Please provide username."}, 400
        return db.searchTrackWeight(username)
    
# use localhost/api/register/{username}/{password}
# will return success if account created, else reutrn fail
api.add_resource(register, "/api/database/register/<string:username>/<string:password>")

# use localhost/api/login/{username}/{password}
# will return success if account is in database, else reutrn fail
api.add_resource(login, "/api/database/login/<string:username>/<string:password>")

api.add_resource(DailyCalories, "/api/database/daily_calories")

api.add_resource(PrintDailyCalories, "/api/database/print_daily_calories")

api.add_resource(TrackWeight, "/api/database/track_weight")

api.add_resource(PrintTrackWeight, "/api/database/print_track_weight")

if __name__ == "__main__":
    db.createDatabase()
    app.run(host='0.0.0.0', port=5011, debug=True)
