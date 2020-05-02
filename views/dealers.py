from flask import Blueprint, request, render_template


dealer_blueprint = Blueprint('dealers', __name__)


@dealer_blueprint.route('/register', methods=['GET'])         #got /dealers/register
def register_dealer():
    if request.method == 'GET':
        return render_template("dealers/register.html")  # This is for Get method
