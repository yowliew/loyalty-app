from typing import Dict
from flask import session
from common.db import db1
from models.ancestor import Ancestor


class StateModel(Ancestor, db1.Model):
    __tablename__ = "state"

    id = db1.Column(db1.Integer, primary_key=True)
    state = db1.Column(db1.String(100), unique=True, index=True, nullable=False)

    def __init__(self, state):
        self.state = state
        self.add_user = session['username']
        self.upd_user = ""  # TODO to be implemented

    def json(self) -> Dict:
        return {
            "state": self.state
        }

    @classmethod
    def find_by_state(cls, state):
        return cls.query.filter_by(state=state).first()

    @classmethod
    def find_all_state(cls):
        return cls.query.all()


class ZipModel(Ancestor, db1.Model):
    __tablename__ = "postcode"

    id = db1.Column(db1.Integer, primary_key=True)
    postcode = db1.Column(db1.String(5), unique=True, index=True, nullable=False)

    def __init__(self, postcode):
        self.postcode = postcode
        self.add_user = "0001"  # TODO to be implemented
        self.upd_user = ""  # TODO to be implemented

    def json(self) -> Dict:
        return {
            "postcode": self.postcode
        }

    @classmethod
    def find_by_postcode(cls, postcode):
        return cls.query.filter_by(postcode=postcode).first()

    @classmethod
    def find_all_postcode(cls):
        return cls.query.all()
