from flask import Blueprint, redirect, url_for, render_template

loyalty_blueprint = Blueprint('loyalty', __name__)


@loyalty_blueprint.route('/', methods=['GET'])  # get /users/login
def the_login():
    return redirect(url_for('users.login_user'))


@loyalty_blueprint.route('/loyalty', methods=['GET'])  # render the landing page
def the_base():
    return render_template("base.html")