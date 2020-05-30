from flask_restful import Resource, reqparse
from flask import jsonify
import re
from models.user import UserModel
from models.dealer import DealerModel
from models.customer import CustomerModel


class Validate(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("method", type=str, required=True, help="Method Error")
    parser.add_argument("value", type=str, required=True, help="Value Error.")

    method = None
    value = None

    def post(self):
        data = self.parser.parse_args()
        self.method = data["method"]
        self.value = data["value"]
        return self.redirect(self.method)

    def redirect(self, method):
        switcher = {
            "username": self.username,
            "password": self.password,
            "dealercode": self.dealercode,
            "dealerregion": self.dealerregion,
            "custPhone": self.custPhone,
            "nothing": lambda: 'XXX'
        }
        func = switcher.get(method, lambda: 'Invalid')
        return func()

    def dealercode(self):
        if DealerModel.find_by_dealer_code(self.value):
            return jsonify({"message": False, "error": "Dealer already exist in the database."})
        else:
            return jsonify({"message": True})

    def dealerregion(self):
        # TODO To be implemented once zipcpode master is ready
        return jsonify({"message": True})

    def username(self):  # Return True only when passed field validate

        if UserModel.find_by_username(self.value):
            return jsonify({"message": False, "error": "User already exist in the database."})
        else:
            return jsonify({"message": True})

    def password(self):
        string_check = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        if string_check.search(self.value) is None:
            return jsonify({"message": False, "error": "Password must contains special character."})
        else:
            return jsonify({"message": True})

    def custPhone(self):
        row = CustomerModel.find_by_customer(self.value)
        if row:
            return jsonify({"cust_name": row.cust_name, "cust_zip": row.cust_zip, "cust_email": row.cust_email})
        else:
            return jsonify({"cust_name": ""})
