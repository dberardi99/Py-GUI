import tkinter as tk
from tkinter import ttk

# def button1_func():
#     print("Hello.")

def change_label():
    # label1.configure(text = "This is a NEW test") # Update first label
    label_1["text"] = entry.get()
    entry["state"] = "disabled"

def reset_label():
    label_1["text"] = "This is a test"
    entry["state"] = "enabled"

# Main window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x700")

# Create widgets (there are both tk and ttk widgets)
label_1 = ttk.Label(
    master = window,
    text = "This is a test")
label_1.pack(pady = 10)

textbox = tk.Text(master = window)
textbox.pack() # Create a textbox

entry = ttk.Entry(master = window)
entry.pack(pady = 10)

frame_1 = ttk.Frame(master = window)
label_2 = ttk.Label(
    master = frame_1,
    text = "My label")
label_2.pack(
    side = "left",
    padx = 10)
# button1 = ttk.Button(master = frame, text = "Press me", command = button1_func).pack(side = "left")
button_1 = ttk.Button(
    master = frame_1,
    text = "Press me",
    command = lambda: print("Hello."))
button_1.pack(side = "left") # It is possible to pass also a lambda function
frame_1.pack(pady = 10)

frame_2 = ttk.Frame(master = window)
button_2 = ttk.Button(
    master = frame_2,
    text = "Change label",
    command = change_label)
button_2.pack(
    side = "left",
    padx = 10)
button_3 = ttk.Button(
    master = frame_2,
    text = "Reset label",
    command = reset_label)
button_3.pack(side = "left")
frame_2.pack(pady = 10)

# Run
window.mainloop() # The mainloop updates both the GUI and checks for events (button clicks, mouse movement, window closing, etc.)
