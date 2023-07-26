from flask import Flask
from flask_restful import Api, Resource
import database as db

app = Flask(__name__)
api = Api(app)


class register(Resource):
    def get(self, username, password):
        if db.checkUsernameIsAvailable(username):
            db.addAccount(username, password)
            return "Success"
        return "Fail"


class login(Resource):
    def get(self, username, password):
        if db.checkAccount(username, password):
            return "Success"
        return "Fail"

api.add_resource(register, "/register/<string:username>/<string:password>")
api.add_resource(login, "/login/<string:username>/<string:password>")

if __name__ == "__main__":
    db.createDatabase()
    app.run(debug=True)
