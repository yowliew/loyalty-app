from typing import Dict
from flask import session
from common.db import db1
from models.ancestor import Ancestor


class CustomerModel(Ancestor, db1.Model):
    __tablename__ = "customers"

    id = db1.Column(db1.Integer, primary_key=True)
    cust_phone = db1.Column(db1.String(100), unique=True, index=True, nullable=False)
    cust_name = db1.Column(db1.String(255), nullable=False)
    gender_type = db1.Column(db1.String(1))
    cust_email = db1.Column(db1.String(100))
    vehicle_type = db1.Column(db1.String(10))
    vehicle_reg = db1.Column(db1.String(10))
    address1 = db1.Column(db1.String(255))
    address2 = db1.Column(db1.String(255))
    cust_state = db1.Column(db1.String(50))
    cust_zip = db1.Column(db1.String(5))
    dealer_code = db1.Column(db1.String(4), db1.ForeignKey("dealers.dealer_code"), nullable=False)
    dealers = db1.relationship("DealerModel")

    def __init__(self, dealer_code, cust_phone, cust_name, gender_type, cust_email, vehicle_type, vehicle_reg,
                 address_1, address_2,
                 cust_state, cust_zip):
        self.cust_phone = cust_phone
        self.cust_name = cust_name
        self.gender_type = gender_type
        self.cust_email = cust_email
        self.vehicle_type = vehicle_type
        self.vehicle_reg = vehicle_reg
        self.address1 = address_1
        self.address2 = address_2
        self.cust_state = cust_state
        self.cust_zip = cust_zip
        self.dealer_code = dealer_code
        self.add_user = session['username']
        self.upd_user = ""  # TODO to be implemented

    def json(self) -> Dict:
        return {
            "cust_phone": self.cust_phone,
            "cust_name": self.cust_name,
            "gender_type": self.gender_type,
            "cust_email": self.cust_email,
            "vehicle_type": self.vehicle_type,
            "vehicle_reg": self.vehicle_reg,
            "address_1": self.address1,
            "address_2": self.address2,
            "cust_state": self.cust_state,
            "cust_zip": self.cust_zip,
            "dealer_code": self.dealer_code
        }

    @classmethod
    def find_by_customer(cls, cust_phone):
        return cls.query.filter_by(cust_phone=cust_phone).first()

    @classmethod
    def find_all_customer(cls):
        return cls.query.all()


class CovidModel(Ancestor, db1.Model):
    __tablename__ = "covid_tracker"

    id = db1.Column(db1.Integer, primary_key=True)
    cust_phone = db1.Column(db1.String(100), index=True, nullable=False)
    cust_temp = db1.Column(db1.Float(2), nullable=False)
    cust_name = db1.Column(db1.String(255), nullable=False)
    cust_zip = db1.Column(db1.String(5))
    cust_email = db1.Column(db1.String(100))
    dealer_code = db1.Column(db1.String(4), db1.ForeignKey("dealers.dealer_code"), nullable=False)
    dealers = db1.relationship("DealerModel")

    def __init__(self, dealer_code, cust_phone, cust_temp, cust_name, cust_zip, cust_email):
        self.cust_phone = cust_phone
        self.cust_temp = cust_temp
        self.cust_name = cust_name
        self.cust_zip = cust_zip
        self.cust_email = cust_email
        self.dealer_code = dealer_code
        self.add_user = session['username']
        self.upd_user = ""  # TODO to be implemented

    def json(self) -> Dict:
        return {
            "cust_phone": self.cust_phone,
            "cust_temp": self.cust_temp,
            "cust_name": self.cust_name,
            "cust_zip": self.cust_zip,
            "cust_email": self.cust_email,
            "dealer_code": self.dealer_code
        }

    @classmethod
    def find_by_covid_phone(cls, cust_phone):
        return cls.query.filter_by(cust_phone=cust_phone).first()

    @classmethod
    def find_all_covid_tracker(cls):
        return cls.query.all()
