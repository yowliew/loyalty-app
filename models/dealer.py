from typing import Dict
from flask import session
from common.db import db1
from models.ancestor import Ancestor


class DealerModel(Ancestor, db1.Model):
    __tablename__ = "dealers"

    id = db1.Column(db1.Integer, primary_key=True)
    dealer_code = db1.Column(db1.String(4), unique=True, index=True, nullable=False)
    dealer_name = db1.Column(db1.String(255), nullable=False)
    dealer_region = db1.Column(db1.String(5), nullable=False)
    dealer_contact = db1.Column(db1.String(100))
    dealer_phone = db1.Column(db1.String(100))
    default = db1.Column(db1.String(1), default='F')

    users = db1.relationship("UserModel", lazy="dynamic")

    def __init__(self, dealer_code, dealer_name, dealer_region, dealer_contact, dealer_phone, default):
        self.dealer_code = dealer_code
        self.dealer_name = dealer_name
        self.dealer_region = dealer_region
        self.dealer_contact = dealer_contact
        self.dealer_phone = dealer_phone
        self.default = default
        self.add_user = session['username']
        self.upd_user = ""  # TODO to be implemented

    def json(self) -> Dict:
        return {
            "dealer_code": self.dealer_code,
            "dealer_name": self.dealer_name,
            "dealer_region": self.regioon,
            "dealer_contact": self.dealer_contact,
            "dealer_phone": self.dealer_phone,
            "default": self.default
        }

    @classmethod
    def find_by_dealer_code(cls, dealer_code):
        return cls.query.filter_by(dealer_code=dealer_code).first()

    @classmethod
    def find_all_dealer(cls):
        return cls.query.all()
