import tkinter as tk
from tkinter import ttk

class GroceryListScreen(tk.Frame):
    def __init__(self, master, pantry):
        super().__init__(master)
        self.configure(background="#FFFFFF")
        self.pantry = pantry

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(side="top", fill="both", expand=True, pady=20)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.configure(background="#FFFFFF")
        
        self.scrollbar = ttk.Scrollbar(self.canvas_frame, command=self.canvas.yview)
        self.grocery_frame = ttk.Frame(self.canvas)

        self.grocery_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.grocery_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.display_inventory()

        self.delete_label = ttk.Label(self, text="Enter the ID Number of the item you want to delete", background="#FFFFFF", foreground="#263238")
        self.delete_entry = ttk.Entry(self)
        self.delete_entry.bind('<Return>', self.on_delete)
        tk.Button(self, text="Delete Items", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=self.delete_item).pack(pady=14, fill=tk.X)

        self.name_label = ttk.Label(self, text="Enter the name of your new item", background="#FFFFFF", foreground="#263238")
        self.name_entry = ttk.Entry(self)
        self.barcode_label = ttk.Label(self, text="Enter the barcode of your new item", background="#FFFFFF", foreground="#263238")
        self.barcode_entry = ttk.Entry(self)
        self.submit_manual = tk.Button(self, text="Submit Item", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=self.on_submit)
        tk.Button(self, text="Add Items", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=self.manual_add).pack(pady=14, fill=tk.X)
        
        tk.Button(self, text="Back", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=master.show_main_screen).pack(fill=tk.X, pady=10)

    def delete_item(self):
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.barcode_label.pack_forget()
        self.barcode_entry.pack_forget()
        self.submit_manual.pack_forget()

        self.delete_label.pack(pady=10)
        self.delete_entry.pack(fill=tk.X, pady=10)
        self.delete_entry.focus()

    def on_delete(self, event):
        id = self.delete_entry.get()
        self.delete_entry.delete(0, tk.END)
        self.pantry.remove_grocery(id)
        self.display_inventory()

    def manual_add(self):
        self.delete_entry.pack_forget()
        self.delete_label.pack_forget()
        self.name_label.pack(pady=5)
        self.name_entry.pack(fill=tk.X, pady=5)
        self.barcode_label.pack(pady=5)
        self.barcode_entry.pack(fill=tk.X, pady=5)
        self.submit_manual.pack(fill=tk.X, pady=10)

    def on_submit(self):
        name = self.name_entry.get().strip()
        barcode = self.barcode_entry.get().strip()

        if name and barcode:
            self.pantry.add_grocery(barcode, name)

        self.name_entry.delete(0, tk.END)
        self.barcode_entry.delete(0, tk.END)

        self.display_inventory()

    def display_inventory(self):
        if len(self.pantry.get_grocery()) != 0:
            max_name_length = max(len(row[2]) for row in self.pantry.get_grocery())


        for widget in self.grocery_frame.winfo_children():
            widget.destroy()

        if len(self.pantry.get_grocery()) == 0:
            ttk.Label(self.grocery_frame, text="Grocery list is currently empty", background="#FFFFFF", foreground="#263238").pack()
        else:
            ttk.Label(self.grocery_frame, text="Current Grocery List:", background="#FFFFFF", foreground="#263238").pack(pady=14)

        for item in self.pantry.get_grocery():
            num, code, name = item
            label_text = f"ID {num}: {code}, {name}"
            ttk.Label(self.grocery_frame, text=label_text, background="#FFFFFF", foreground='#263238', width=max_name_length + 14, font=('Helvetica', 10)).pack()

