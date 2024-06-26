###########################################################
# user_interface.py
# Jack Holscher
#
# Defines the main frame of the user interface for the
# smart pantry application
###########################################################

import tkinter as tk
from tkinter import ttk
from edit_inventory_screen import EditInventoryScreen
from recipe_screen import RecipeScreen
from grocery_list_screen import GroceryListScreen
from scan_items_screen import ScanItemsScreen

import sys
import os
current_dir = os.path.dirname(__file__)
backend_dir = os.path.abspath(os.path.join(current_dir, '..', 'backend'))
sys.path.insert(0, backend_dir)
from pantry_class import Pantry
pantry = Pantry()

class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Pantry")
        self.MAX_WIDTH = 1200
        self.MAX_HEIGHT = 800

        self.style = ttk.Style(self)
        self.configure(background="#FFFFFF")
        self.style.configure('TLabel', font=('Helvetica', 14))
        self.style.configure('TEntry', font=('Helvetica', 12), padding=10)
        self.style.configure("TFrame", background="#FFFFFF")

        self.current_screen = None
        self.init_window()

    def init_window(self):
        screen_wid = self.winfo_screenwidth()
        screen_hit = self.winfo_screenheight()

        x = int((screen_wid / 2) - (self.MAX_WIDTH / 2))
        y = int((screen_hit / 2) - (self.MAX_HEIGHT / 2))
        
        self.geometry(f'{self.MAX_WIDTH}x{self.MAX_HEIGHT}+{x}-{y}')
        self.show_main_screen()
        

    def show_screen(self, frame_class, *args, **kwargs):
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.current_screen = frame_class(self, *args, **kwargs)
        self.current_screen.pack()

    def show_main_screen(self):
        self.show_screen(MainScreen)

class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background="#FFFFFF")
        ttk.Label(self, text="Welcome to your Smart Pantry!", background="#FFFFFF", foreground='#263238', padding=30).pack(fill=tk.X)
        tk.Button(self, text="Scan Items", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=lambda: master.show_screen(ScanItemsScreen, pantry)).pack(fill=tk.X, pady=20)
        tk.Button(self, text="Edit Inventory", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=lambda: master.show_screen(EditInventoryScreen, pantry)).pack(fill=tk.X, pady=20)
        tk.Button(self, text="Generate Recipe", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=lambda: master.show_screen(RecipeScreen)).pack(fill=tk.X, pady=20)
        tk.Button(self, text="View Grocery List", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=lambda: master.show_screen(GroceryListScreen)).pack(fill=tk.X, pady=20)

if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()
