import os
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
from common.security import authenticate, identity
from common.end_route import api_end_route, blueprint_end_route

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.secret_key = "somesecret_key123"

api = Api(app)
jwt = JWT(app, authenticate, identity)

api_end_route(api)
blueprint_end_route(app)

if __name__ == "__main__":
    from common.db import db1

    db1.init_app(app)


    @app.before_first_request
    def create_dbstruc():
        db1.create_all()


    app.run(debug=True)
