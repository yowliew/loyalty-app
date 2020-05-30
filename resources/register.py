from flask import jsonify
from flask_restful import Resource, reqparse
from models.user import UserModel
from models.dealer import DealerModel
from models.customer import CustomerModel, CovidModel
from common.db import db1


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username", type=str, required=True, help="Username Error.")
    parser.add_argument("password", type=str, required=True, help="Password Error.")
    parser.add_argument("dealer_code", type=str, required=True, help="Dealer code Error.")

    # parser.add_argument("username", type=str, required=True, help="Error: {error_msg}")
    # parser.add_argument("password", type=str, required=True, help="Password Error.")
    # parser.add_argument("dealer_code", type=str, required=True, help="Dealer code Error.")
    #
    # {
    #     "message": {"username": "Error : Username is not a valid choice"}
    # }

    def post(self):
        data = self.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return jsonify({"message": "User already exist in the database."})

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


class CustomerRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("dealer_code", type=str, required=True, help="Dealer Code Error.")
    parser.add_argument("cust_phone", type=str, required=True, help="Customer Phone Error.")
    parser.add_argument("cust_name", type=str, required=True, help="Customer Name Error.")
    parser.add_argument("gender_type", type=str, required=True, help="Gender Error.")
    parser.add_argument("cust_email", type=str, help="Email Error.")
    parser.add_argument("vehicle_type", type=str, required=True, help="Vehicle Type Error.")
    parser.add_argument("vehicle_reg", type=str, required=True, help="Vehicle Registration Error.")
    parser.add_argument("address_1", type=str, help="Address Error.")
    parser.add_argument("address_2", type=str, help="Address Error.")
    parser.add_argument("cust_state", type=str, help="State Error.")
    parser.add_argument("cust_zip", type=str, help="Zipcode Error.")

    def post(self):
        data = self.parser.parse_args()

        if CustomerModel.find_by_customer(data["cust_phone"]):
            return jsonify({"message": "Customer already exits in the database"})

        customer = CustomerModel(**data)
        customer.save_to_db()

        return jsonify({"message": "Customer Registered !"})


class CovidRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("dealer_code", type=str, required=True, help="Dealer Code Error.")
    parser.add_argument("cust_phone", type=str, required=True, help="Customer Phone Error.")
    parser.add_argument("cust_temp", type=float, required=True, help="Customer Body Temperature Error.")
    parser.add_argument("cust_name", type=str, help="Customer Name Error.")
    parser.add_argument("cust_zip", type=str, help="Zipcode Error.")
    parser.add_argument("cust_email", type=str, help="Email Error.")

    def post(self):
        data = self.parser.parse_args()

        customer = CustomerModel.find_by_customer(data["cust_phone"])

        if not customer:  # Create new customer
            customer = CustomerModel(dealer_code=data['dealer_code'], cust_phone=data['cust_phone'],
                                     cust_name=data['cust_name'], gender_type=None,
                                     cust_email=data['cust_email'], vehicle_type=None, vehicle_reg=None, address_1=None,
                                     address_2=None, cust_state=None,
                                     cust_zip=data['cust_zip'])
        else:
            customer.cust_name = data['cust_name']  # Edit customer detail to update customer table
            customer.cust_zip = data['cust_zip']
            customer.cust_email = data['cust_email']

        customer.save_to_db()

        covid_customer = CovidModel(**data)
        covid_customer.save_to_db()

        return jsonify({"message": "Customer Registered !"})
