from flask import Flask
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
        return {"Failed":f"Login Failed"}
# use localhost/register/{username}/{password}
# will return success if account created, else reutrn fail
api.add_resource(register, "/register/<string:username>/<string:password>")


# use localhost/login/{username}/{password}
# will return success if account is in database, else reutrn fail
api.add_resource(login, "/login/<string:username>/<string:password>")

if __name__ == "__main__":
    db.createDatabase()
    app.run(host='0.0.0.0', port=5011, debug=True)
