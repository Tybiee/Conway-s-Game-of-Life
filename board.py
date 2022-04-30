import tkinter as tk

tk = tk.Tk()
tk.title("Conway's Game of Life")

# Window dimensions
window_width = 500
window_height = 500

# Screen dimensions
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

# Center location
center_x = int(screen_width/2-window_width/2)
center_y = int(screen_height/2-window_height/2)

# Sets window to center screen
tk.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Resize denied
tk.resizable(False, False)

# Icon
tk.iconbitmap('./assets/life.ico')