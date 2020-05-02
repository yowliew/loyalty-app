from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        data = StoreModel.find_by_name(name)
        if data:
            return data.json(), 200
        return {"message" : "Store not found"}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message" : "Store {} already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message" : "Encounter error creating new store"}, 500
        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {"message": "Store {} not found".format(name)}, 404
        print(store)

        try:
            store.delete_from_db()
        except:
            return {"message": {"Encounter error while deleting store"}}, 500
        return {"message": "Store {} been deleted".format(name)}, 200


class StoreList(Resource):

    def get(self):
        return {"store" : [store.json() for store in StoreModel.query.all()]}, 200