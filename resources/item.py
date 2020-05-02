from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()  # parse the payload and validate based on the condition
    parser.add_argument("price", type=float, required=True, help="The field 'price' not satisfied the condition")
    parser.add_argument("store_id", type=int, required=True, help="The field 'store_id' not satisfied the condition")


    @jwt_required()
    def get(self, name):
        data = ItemModel.find_by_name(name)
        if data:
            return data.json(), 200
        return {"message":"Item not found"}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message" : "{} already exist.".format(name)}, 400

        data = self.parser.parse_args()

#        item = ItemModel(name, data["price"], data["store"])
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message" : "An error occurred inserting the item"}, 500
        return item.json(), 201


    def put(self, name):
        requested_data = self.parser.parse_args()           #Use self to call the parse at Item class level

        item = ItemModel.find_by_name(name)

        if item is None :
             item = ItemModel(name, **requested_data)
        else:
             item.price = requested_data["price"]

        item.save_to_db()
        return item.json(), 200


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message" : "Item deleted!"}


class ItemList(Resource):
    def get(self):
        return{"item": [item.json() for item in ItemModel.query.all()]}, 200
#       return{"item" : list(map(x:x.json(), ItemModel.query.all()))}, 200

