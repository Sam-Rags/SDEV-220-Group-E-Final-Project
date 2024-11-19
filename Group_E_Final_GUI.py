'''
Author: Samuel Ragsdale
Date started: 11/17/2024
Assignment: GUI Outline for SDEV220 Final Project
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
import os



scriptDirectory = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptDirectory)

root = tk.Tk()
style=ttk.Style(root)
style.theme_use('winnative')
style.configure('.', font=('MS Serif', 16))
style.configure('TButton', background='#1fcc81', foreground='#1fcc81')
style.configure('TLabel', background='#2a3b4c', foreground="white")

root.title("Placeholder")
#root.geometry("1366x768")
root.config(bg = "#2a3b4c")

image = Image.open("generic-logo.jpg")
newSize = (200, 66)
resizedImage = image.resize(newSize, PIL.Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resizedImage)
imageLabel = tk.Label(root, image = photo, bd = 0)
imageLabel.grid(row=0, column=0)

searchLabel = ttk.Label(root, text="Search Customers, Inventory, or Orders:")
searchLabel.grid(column=1, row=0, pady=20)

searchMenu = ttk.Combobox(root, font=('MS Serif', 16), width=10, values=("Customer", "Inventory", "Orders"))
searchMenu.grid(column=2, row=0, padx=(0,200), pady=20)

searchBar = ttk.Entry(root, width=22, font=('MS Serif', 16))
searchBar.grid(column=2, row=0, padx=(200,0), pady=20)

searchButton = ttk.Button(root, text="Search")
searchButton.grid(column=3, row=0, padx=(0,20), pady=20)



outputCanvas = tk.Canvas(root, height=400, width=800)
outputCanvas.grid(column=1, row=1, columnspan=2, padx=20)



newItemButton = ttk.Button(root, width=20, text="Add New Item")
newItemButton.grid(column=0, row=1, padx=15, pady=(0,250))

newOrderButton = ttk.Button(root, width=20, text="Add New Order")
newOrderButton.grid(column=0, row=1, padx=15, pady=(0,340))

newCustomerButton = ttk.Button(root, width=20, text="Add New Customer")
newCustomerButton.grid(column=0, padx=15, row=1, pady=(0,160))

exitButton = ttk.Button(root, text="Quit Program", width=20, command=root.destroy)
exitButton.grid(column=0, row=99, pady=20)

root.mainloop()