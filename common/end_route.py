# import for api
from resources.register import UserRegister, DealerRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# import for blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from views.dealers import dealer_blueprint


def api_end_route(api):
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(Store, "/stores/<string:name>")
    api.add_resource(StoreList, "/stores")
    api.add_resource(UserRegister, "/user_register")
    api.add_resource(DealerRegister, "/dealer_register")


def blueprint_end_route(app):
    app.register_blueprint(store_blueprint, url_prefix="/stores")
    app.register_blueprint(user_blueprint, url_prefix="/users")
    app.register_blueprint(dealer_blueprint, url_prefix="/dealers")
