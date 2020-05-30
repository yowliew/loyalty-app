from flask_restful import Resource, reqparse
from flask import session, jsonify
from models.master import StateModel, ZipModel


class Logout(Resource):
    def get(self):
        session["username"] = None
        return jsonify({"message": True})


class AutoComplete(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("field", type=str, required=True, help="Field Error.")

    field = None

    def post(self):
        data = self.parser.parse_args()
        self.field = data["field"]
        return self.redirect(self.field)

    def redirect(self, field):
        switcher = {
            "state": self.state,
            "postcode": self.postcode,
            "nothing": lambda: 'XXX'
        }
        func = switcher.get(field, lambda: 'Invalid')
        return func()

    def state(self):
        states = StateModel.find_all_state()
        return jsonify({"state": [state.json() for state in states]})

    def postcode(self):
        postcodes = ZipModel.find_all_postcode()
        return jsonify({"postcode": [postcode.json() for postcode in postcodes]})
