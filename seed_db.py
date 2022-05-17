"""Script to seed database."""

import os
import model
import server


os.system("dropdb my_inventory")
os.system("createdb my_inventory")

model.connect_to_db(server.app)
model.db.create_all()
