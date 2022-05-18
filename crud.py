from model import Item, Owner, connect_to_db,db

def create_item(type, name, quantity, owner):
    """Create and return a new item."""

    new_item = Item(item_type=type, item_name=name, quantity=quantity, owner=owner)

    return new_item


def get_item_list():
    """Show all items"""

    return Item.query.all()


def get_item_by_id(item_id):
    """Return an item with a specific id"""

    return Item.query.get(item_id)

def get_item_by_name(item_name):
    """Return an item with a specific name"""

    return Item.query.filter(Item.item_name==item_name).first()

def create_owner(name):
    """Create and return a new owner"""
    
    new_owner = Owner(owner_name=name)
    return new_owner
    
def get_owner_by_name(name):
    """Take a movie_id as an argument and return the movie with that ID."""

    return Owner.query.filter(Owner.owner_name==name).first()

if __name__ == '__main__':
    from main import app
    connect_to_db(app)



