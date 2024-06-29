#####################################################
# pantry.py
# Jack Holscher
#
# Defines the pantry class that will manage and
# access the inventory of the items added to the
# smart pantry
#####################################################

from database import Database, GroceryListDatabase
from model_client import OpenAIClient

import openfoodfacts
api = openfoodfacts.API(user_agent="smart-pantry/1.0")

class Pantry():
    def __init__(self):
        self.db = Database("smart_pantry.db")
        self.grocery_db = GroceryListDatabase("grocery_list.db")  
        self.target_info = ["product_name"]
        self.client = OpenAIClient.get_instance().get_client()

    def add_item(self, code, name=None):
        if name is None:
            food_data = api.product.get(code, fields=self.target_info)
            self.db.add_item(code, food_data["product_name"])
        else:
            self.db.add_item(code, name)
            
    def remove_item(self, id):
        removed = self.get_item(id)
        self.add_grocery(removed[1], removed[2])

        self.db.remove_item(id)

    def get_item(self, id):
        return self.db.get_item(id)

    def get_inventory(self):
        return self.db.get_inventory()
    
    def get_grocery(self):
        return self.grocery_db.get_grocery()
    
    def add_grocery(self, code, name):
        self.grocery_db.add_item(code, name)

    def remove_grocery(self, id):
        self.grocery_db.remove_item(id)

    def close_pantry(self):
        self.db.close()

    def close_grocery(self):
        self.grocery_db.close()

    def get_recipe_from_ingredients(self, ingredients):
        sys_prompt = "You are a helpful assitant skilled in recommending detailed recipes from an ingredient list"
        user_prompt = f"Generate a recipe from this list of ingredients: {', '.join(ingredients)}. You don't have to include every ingredient, just the ones necessary to make the recipe that you recommend."
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages= [
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt},
                ]
            )
        except:
            return "API Error..."
        
        output = response.choices[0].message.content
        return output