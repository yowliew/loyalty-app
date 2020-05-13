from flask import Blueprint, request, session, url_for, render_template, redirect, flash
from models.user import UserModel

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            UserModel.is_user_valid(username=username, password=password)
            session['username'] = username
            return redirect(url_for('loyalty.the_base'))
        except Exception as e:
            flash(f"Error {e}", category="warning")
            return render_template("users/login.html")
        s
    return render_template("users/login.html")  # Send the user an error if their login was invalid


@user_blueprint.route('/register', methods=['GET'])  # get /users/register
def register_user():
    if request.method == 'GET':
        return render_template("users/register.html")  # This is for Get method
