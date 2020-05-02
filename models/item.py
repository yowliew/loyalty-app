from common.db import db1

class ItemModel(db1.Model):
    __tablename__ = "items"

    id = db1.Column(db1.Integer, primary_key = True)
    item_name = db1.Column(db1.String(80))
    price = db1.Column(db1.Float(precision=2))
    store_id = db1.Column(db1.Integer, db1.ForeignKey("stores.id"))

    store1 = db1.relationship("StoreModel")     # reference to the stores table

    def __init__(self, name, price, store_id):
        self.item_name = name
        self.price = price
        self.store_id = store_id


    def json(self):
        return {"item_name" : self.item_name, "price" : self.price, "store_id" : self.store_id}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(item_name = name).first()


    def save_to_db(self):
        db1.session.add(self)
        db1.session.commit()


    def delete_from_db(self):
        db1.session.delete(self)
        db1.session.commit()
