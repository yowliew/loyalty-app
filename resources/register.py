from flask import jsonify
from flask_restful import Resource, reqparse
from models.user import UserModel
from models.dealer import DealerModel
from common.db import db1


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username Error.")
    parser.add_argument("password", type=str, required=True, help="Password Error.")
    parser.add_argument("dealer_code", type=str, required=True, help="Dealer code Error.")

    def post(self):
        data = self.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return jsonify({"message": "User already exist in the database"})

        user = UserModel(**data)
        user.save_to_db()

        return jsonify({"message": "User created successfully."})

    def get(self):
        # row = db1.session.query(db1.func.max(UserModel.user_code)).scalar()
        row = db1.session.query(DealerModel).filter(DealerModel.default == "T").first()
        return jsonify({"dealer_code": row.dealer_code, "dealer_name": row.dealer_name})


class DealerRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("dealer_code", type=str, required=True, help="Dealer code Error.")
    parser.add_argument("dealer_name", type=str, required=True, help="Dealer name Error.")
    parser.add_argument("dealer_region", type=str, required=True, help="Dealer region Error.")
    parser.add_argument("dealer_contact", type=str, required=True, help="Dealer contact Error.")
    parser.add_argument("dealer_phone", type=str, required=True, help="Dealer phone Error.")
    parser.add_argument("default", type=str, required=True, help="Default flag Error.")

    def post(self):
        data = self.parser.parse_args()

        if DealerModel.find_by_dealer_code(data["dealer_code"]):
            return jsonify({"message": "Dealer already exist in the database"})

        dealer = DealerModel(**data)
        dealer.save_to_db()

        return jsonify({"message": "Dealer created successfully."})
