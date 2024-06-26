import tkinter as tk
from tkinter import ttk

class GroceryListScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background="#FFFFFF")
        ttk.Label(self, text="Here is your current grocery list:", background='#FFFFFF', foreground='#263238', padding=10).pack(fill=tk.X)
        tk.Button(self, text="Back", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=master.show_main_screen).pack(fill=tk.X, pady=10)