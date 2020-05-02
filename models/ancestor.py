from common.db import db1
from sqlalchemy.sql import func

class Ancestor(object):
    __tablename__ = None

    add_date = db1.Column(db1.DateTime(timezone=True), nullable =False, server_default = func.now())
    upd_date = db1.Column(db1.DateTime(timezone=True), onupdate= func.now())
    add_user = db1.Column(db1.String(8))
    upd_user = db1.Column(db1.String(8))

    def save_to_db(self):
        db1.session.add(self)
        db1.session.commit()


    def delete_from_db(self):
        db1.session.delete(self)
        db1.session.commit()
