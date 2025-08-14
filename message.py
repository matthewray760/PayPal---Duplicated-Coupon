import tkinter as tk
from tkinter import messagebox


def show_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Info", message)  # Show the message box
    root.destroy()  # Destroy the root window after closing the message box
