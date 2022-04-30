import tkinter as tk
import cell

root = tk.Tk()
root.title("Conway's Game of Life")

# Window dimensions
window_width = 504
window_height = 490

# Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Center location
center_x = int(screen_width/2-window_width/2)
center_y = int(screen_height/2-window_height/2)

# Sets window to center screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Resize denied
root.resizable(False, False)

# Grid
root.columnconfigure(0, weight=1)

for r in range(14):
   for c in range(14):
       empty = tk.Label(root, text='    ',font=('Arial',18), background='black')
       empty.grid(column=c, row=r, sticky=tk.W, padx=1, pady=1)

# Icon
root.iconbitmap('./assets/life.ico')