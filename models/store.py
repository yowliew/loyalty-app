from common.db import db1
from models.ancestor import Ancestor

class StoreModel(Ancestor, db1.Model):
    __tablename__ = "stores"

    id = db1.Column(db1.Integer, primary_key = True)
    store_name = db1.Column(db1.String(80))

    items = db1.relationship("ItemModel", lazy = "dynamic")       # reference to the items table
                                                                #lazy = dynamic is to ask no to create the items yet!!
    def __init__(self, name):
        self.store_name = name
        self.add_user = "Liew"


    def json(self):
        return {"store_name" : self.store_name,
                "add_date" : str(self.add_date),
                "add_user": self.add_user,
                "items" :[item.json() for item in self.items.all() ]}


    @classmethod
    def find_by_name(cls,  name):
        return cls.query.filter_by(store_name=name).first()

