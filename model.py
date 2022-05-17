"""Models for inventory tracking web application"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    """An inventory of items"""

    __tablename__ = "item"

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(100), nullable=False)
    series_id = db.Column(db.String(50), nullable=False)
    quantity = db.db.Column(db.Integer, default=0)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.owner_id"), nullable=False)
    
    owner = db.relationship("Owner", back_populates="items")
    

    def __repr__(self):
        """Show item id and item quantity"""

        return f"<item_id: {self.item_id} quantity: {self.quantity}>"


class Owner(db.Model):
    """An owner of items"""

    __tablename__ = "owner"

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    registered_number = db.Column(db.String(100), nullable=False)
    
    items = db.relationship("Item", back_populates="owner")
    

    def __repr__(self):
        """Show owner id and name"""

        return f"<owner_id: {self.owner_id} owner_name: {self.name}>"


def connect_to_db(flask_app, db_uri="postgresql:///my_inventory", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)


