import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk # ttkbootstrap takes all of the ttk widgets and add more styling options

def convert():
    mile_input = entry_int.get() # Get data
    km_output = mile_input * 1.61 # Conversion
    output_string.set(km_output) # Update widget

# Create main window where to put everything on
# window = tk.Tk()
window = ttk.Window(themename = "darkly")
w = int(window.winfo_screenwidth() / 5)
h = int(window.winfo_screenheight() / 5)
window.title("Demo")
window.geometry(f"{w}x{h}") # width x height in pixels

# Create the first widget (namely the GUI's title)
# Widgets (text, buttons, checkboxes, menus, frames, etc.) are the building blocks of tkinter
title_label = ttk.Label(master = window,
                        text = "Miles to Kilometers",
                        font = "Calibri 24 bold")
title_label.pack() # Place the label on the specified window

# Create the input field (which is a widget too)
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame,
                  textvariable = entry_int)
button = ttk.Button(master = input_frame,
                    text = "Convert",
                    command = convert)
entry.pack(side = "left", padx = 10) # The side argument is needed to have entry and button next each other (padx is the gap between the two)
button.pack(side = "left")
input_frame.pack(pady = 10) # Firstly place entry and button inside the frame and then place the frame into the window

# Create the output (which is again a widget)
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                         text = "Output",
                         font = "Calibri 24",
                         textvariable = output_string)
output_label.pack(pady = 5)

# Run
window.mainloop()
