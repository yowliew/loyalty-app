from flask import Blueprint, request, session, url_for, render_template, redirect
# from models.user import User, UserErrors


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    pass
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']
    #
    #     try:
    #         if User.is_login_valid(email, password):
    #             session['email'] = email
    #             return redirect(url_for('alerts.index'))
    #     except UserErrors.UserError as e:
    #         return e.message

    return render_template("users/login.html")  # Send the user an error if their login was invalid


@user_blueprint.route('/register', methods=['GET'])         #get /users/register
def register_user():
    if request.method == 'GET':
        return render_template("users/register.html")  # This is for Get method
