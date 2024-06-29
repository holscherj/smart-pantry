import tkinter as tk
from tkinter import ttk

class RecipeScreen(tk.Frame):
    def __init__(self, master, pantry):
        super().__init__(master)
        self.pantry = pantry
        self.configure(background="#FFFFFF")

        ttk.Label(self, text="Here is a recipe based on what we found in your pantry:", background='#FFFFFF', foreground='#263238', padding=10).pack(fill=tk.X)

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(side="top", fill="both", expand=True, pady=20)

        self.canvas = tk.Canvas(self.canvas_frame, width=800, height= 400)
        self.canvas.configure(background="#FFFFFF")
        
        self.scrollbar = ttk.Scrollbar(self.canvas_frame, command=self.canvas.yview)
        self.recipe_frame = ttk.Frame(self.canvas)

        self.recipe_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.recipe_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        ingredients = [item[2] for item in self.pantry.get_inventory()]
        recipe = self.pantry.get_recipe_from_ingredients(ingredients)
        ttk.Label(self.recipe_frame, text=recipe,  background="#FFFFFF", foreground='#263238', font=('Helvetica', 10), wraplength=780).pack()

        tk.Button(self, text="Back", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=master.show_main_screen, width=40).pack(pady=10)

