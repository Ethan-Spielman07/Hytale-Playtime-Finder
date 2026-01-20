import tkinter as tk
from tkinter import ttk
import getpass
import os
from find_playtime import find_playtime

worlds = []
username = getpass.getuser()
folder_path = rf"C:\Users\{username}\AppData\Roaming\Hytale\UserData\Saves"

for filename in os.listdir(folder_path):
    worlds.append(filename)

text_font = ("Arial", 10, "bold")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    
root = tk.Tk()

root.title("Hytale Playtime Finder")
root.geometry("300x100")
root.configure(bg = "dark slate gray")
center_window(root)
root.resizable(False, False)

frame = tk.Frame(root, width = 300, height = 100, bg = "dark slate gray")
frame.pack(fill = "both")

tk.Label(frame, text = "Select a world:", bg = "dark slate gray", fg = "white", font = text_font).pack()

style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox", fieldbackground = "light slate gray", background = "light slate gray")

style.map("TCombobox", selectbackground = [("readonly", "light slate gray")], selectforeground = [("readonly", "black")])

world_selection = ttk.Combobox(frame, values = worlds)
world_selection.pack(pady = 5)

playtime = ""
playtime_label = tk.Label(frame, text = "", bg = "dark slate gray", fg = "white", font = text_font)
playtime_label.pack(pady = 5)

def on_select(event):
    playtime = "Playtime: " + find_playtime(world_selection.get())
    playtime_label.config(text = playtime)

world_selection.bind("<<ComboboxSelected>>", on_select)

root.mainloop()