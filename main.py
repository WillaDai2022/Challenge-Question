from flask import Flask, render_template,request,redirect,flash
# from model import connect_to_db
import crud
app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage"""
    return render_template("home.html")

@app.route("/add")
def add_item_page():
    """User input the info of the item which is going to be added"""
    return render_template("add_item.html")

@app.route("/add_item", methods=["POST"])
def add_item():
    """Add a new item"""

    item_name = request.form.get("item_name")
    quantity = int(request.form.get("item_quantity"))
    owner_name = request.form.get("owner_name")

    owner = crud.get_owner_by_name(owner_name)
    print("##########################")
    print("owner")
    if not owner:
        owner = crud.create_owner(owner_name)

    curr_item = crud.get_item_by_name(item_name)
    if curr_item:
        curr_item.quantity += quantity
    else:
        type = request.form.get("item_type")
        new_item = crud.create_item(type, item_name,quantity, owner)
        crud.db.session.add(new_item)
        print("**************")

    crud.db.session.commit()
    flash("Added")
     
    return redirect("/add_item")

    
@app.route("/view_all_items")
def show_all_items():
    """Show all the inventory items"""
    items = crud.get_item_list
    if not items:
        items = ["no"]
    return render_template("view_all_items.html")


if __name__ == "__main__":
    # connect to database before app.run gets called. 
    # If not, Flask won’t be able to access your database
    app.run(host='0.0.0.0', port=8080)
