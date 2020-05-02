from app import app
from common.db import db1

db1.init_app(app)

@app.before_first_request
def create_dbstruc():
    db1.create_all()
