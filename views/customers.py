from flask import Blueprint, request, render_template, flash

customer_blueprint = Blueprint('customers', __name__)
covid_blueprint = Blueprint('covidtracker', __name__)


@customer_blueprint.route('/register', methods=['GET'])  # get /users/register
def register_customer():
    if request.method == 'GET':
        return render_template("customers/register.html")  # This is for Get methods


@covid_blueprint.route('/tracker', methods=['GET'])  # get /users/register
def covid_tracker():
    if request.method == 'GET':
        return render_template("customers/covidregister.html")  # This is for Get method