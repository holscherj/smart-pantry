import tkinter as tk
from tkinter import ttk

class ScanItemsScreen(tk.Frame):
    def __init__(self, master, pantry):
        super().__init__(master)
        self.pantry = pantry
        self.configure(background="#FFFFFF")

        self.inventory_frame = ttk.Frame(self)
        self.inventory_frame.pack(fill=tk.BOTH, expand=True)
        self.display_inventory()

        self.entry = ttk.Entry(self)
        self.entry.bind('<Return>', self.on_enter)
        self.stop_button = tk.Button(self, text="Stop Scanning", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=self.stop_scan)

        self.scan_button = tk.Button(self, text="Scan Items", bg="#1E88E5", fg="white", font=('Helvetica', 12), command=self.start_scan)
        self.scan_button.pack(fill=tk.X, pady=10)

    def start_scan(self):
        self.scan_button.pack_forget()
        self.entry.pack(fill=tk.X, pady=10)
        self.entry.focus()
        self.stop_button.pack(fill=tk.X, pady=10)
        self.is_scanning = True
        self.scan_loop()

    def stop_scan(self):
        self.is_scanning = False
        self.master.show_main_screen()

    def scan_loop(self):
        if self.is_scanning:
            if self.entry.get():
                barcode = self.entry.get()
                self.process_scan(barcode)
                self.entry.delete(0, tk.END)
            self.after(100, self.scan_loop)

    def on_enter(self, event):
        barcode = self.entry.get()
        if barcode:
            self.process_scan(barcode)
            self.entry.delete(0, tk.END)

    def process_scan(self, barcode):
        self.pantry.add_item(barcode)
        self.display_inventory()

    def display_inventory(self):
        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        if len(self.pantry.get_inventory()) == 0:
            ttk.Label(self.inventory_frame, text="Inventory is currently empty", background="#FFFFFF", foreground="#263238").pack()
        else:
            ttk.Label(self.inventory_frame, text="Current inventory:", background="#FFFFFF", foreground="#263238").pack()

        for item in self.pantry.get_inventory():
            id, code, name = item
            ttk.Label(self.inventory_frame, text=f"{id}: Barcode: {code}, Name: {name}", background="#FFFFFF", foreground='#263238').pack()