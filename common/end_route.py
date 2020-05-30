# import for api
from resources.register import UserRegister, DealerRegister, CustomerRegister, CovidRegister
from resources.validate import Validate
from resources.misc import Logout, AutoComplete
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# import for blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from views.dealers import dealer_blueprint
from views.customers import customer_blueprint, covid_blueprint
from views.loyalty import loyalty_blueprint


def api_end_route(api):
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(Store, "/stores/<string:name>")
    api.add_resource(StoreList, "/stores")
    api.add_resource(UserRegister, "/user_register")
    api.add_resource(DealerRegister, "/dealer_register")
    api.add_resource(CustomerRegister, "/customer_register")
    api.add_resource(CovidRegister, "/covid_tracker")
    api.add_resource(Validate, "/validate_field")
    api.add_resource(Logout, "/logout")
    api.add_resource(AutoComplete, "/autocomplete")


def blueprint_end_route(app):
    app.register_blueprint(loyalty_blueprint, url_prefix="/")
    app.register_blueprint(store_blueprint, url_prefix="/stores")
    app.register_blueprint(user_blueprint, url_prefix="/users")
    app.register_blueprint(dealer_blueprint, url_prefix="/dealers")
    app.register_blueprint(customer_blueprint, url_prefix="/customers")
    app.register_blueprint(covid_blueprint, url_prefix="/covid_tracker")