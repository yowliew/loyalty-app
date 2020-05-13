from flask_restful import Resource, reqparse
from flask import session, jsonify


class Logout(Resource):
    def get(self):
        session["username"] = None
        return jsonify({"message": True})
