from model import db, Item, Owner, connect_to_db

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


def create_owner(owner_name, registered_number):
    """Create and return a new owner"""
    
    new_owner = Owner(owner_name=owner_name, registered_number=registered_number)

    return new_owner




