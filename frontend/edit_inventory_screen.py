import tkinter as tk
from tkinter import ttk

class EditInventoryScreen(tk.Frame):
    def __init__(self, master, pantry):
        super().__init__(master)
        self.pantry = pantry
        self.configure(background="#FFFFFF")
        
        ttk.Label(self, text="Inventory Items:", background="#FFFFFF", foreground='#263238', padding=20).pack()
        for item in self.pantry.get_inventory():
            code, name = item
            ttk.Label(self, text=f"{code}: {name}", background="#FFFFFF", foreground='#263238').pack()

        tk.Button(self, text="Back", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=master.show_main_screen).pack(fill=tk.X)