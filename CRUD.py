from model import db, Item,connect_to_db

def create_item(email, password, phone, fname, lname):
    """Create and return a new user account."""

    account = Account(email=email, password=password, phone=phone, fname=fname, lname=lname, photo = f"/static/image/backgrounds/no-photo.png")

    return account


def get_accounts():
    """Show all the user accounts"""

    return Account.query.all()


def get_account_by_id(account_id):
    """Return a user account with a specific id"""

    return Account.query.get(account_id)

