#####################################################
# pantry.py
# Jack Holscher
#
# Defines the pantry class that will manage and
# access the inventory of the items added to the
# smart pantry
#####################################################

from database import Database
import openfoodfacts
api = openfoodfacts.API(user_agent="smart-pantry/1.0")

class Pantry():
    def __init__(self):
        self.db = Database("smart_pantry.db")
        self.target_info = ["product_name"]
    
    def add_item(self, code, name=None):
        if name is None:
            food_data = api.product.get(code, fields=self.target_info)
            self.db.add_item(code, food_data["product_name"])
        else:
            self.db.add_item(code, name)
            
    def remove_item(self, id):
        self.db.remove_item(id)

    def get_item(self, code):
        self.db.get_item(code)

    def get_inventory(self):
        return self.db.get_inventory()

    def close_pantry(self):
        self.db.close()