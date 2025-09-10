import tkinter as tk
from tkinter import ttk

def button_1_func():
    print(string_var.get())
    string_var.set("Button pressed")

def button_2_func():
    print(radio_var.get())

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

def button_4_func(entry_str):
    print(entry_str.get())

# Window
window = tk.Tk()
window.title("Tkinter Variables and Buttons")
window.geometry("600x600")

# Tkinter variables (there are string vars, double vars and boolean vars)
string_var = tk.StringVar(value = "Test")
button_string = tk.StringVar(value = "A button with string var")

# Widgets
label = ttk.Label(
    master = window,
    text = "Label",
    textvariable = string_var) # The text field is overwritten by the textvariable
label.pack()

entry_1 = ttk.Entry(
    master = window,
    textvariable = string_var)
entry_1.pack()

entry_2 = ttk.Entry(
    master = window,
    textvariable = string_var)
entry_2.pack()

button_1 = ttk.Button(
    master = window,
    text = "Button",
    command = button_1_func)
button_1.pack()

# Buttons (there are buttons, checkbuttons and radiobuttons... they are always widgets)
button_2 = ttk.Button(
    window,
    text = "A simple button",
    command = button_2_func,
    textvariable = button_string)
button_2.pack()

check_var = tk.IntVar() # We need an external variable to retrieve the state of a checkbutton
check_1 = ttk.Checkbutton(
    window,
    text = "Checkbox 1",
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = -10)
check_1.pack()

check_2 = ttk.Checkbutton(
    window,
    text = "Checkbox 2",
    command = lambda: check_var.set(-10)) # With check and radio buttons an external variable is needed to retreive their value
check_2.pack() # Checkbutton 2 switch off (see -10) the checkbutton 1 when pressed (checkbuttons need to be manually connected, while radiobuttons are always connected)

radio_var = tk.StringVar() # Since the types of the two radio values are string and int it is better to opt for a string type (the integer will be converted to string)
radio_1 = ttk.Radiobutton(
    window,
    text = "Radiobutton 1",
    value = "Hello, I'm radiobutton 1",
    command = lambda: print(radio_var.get()),
    variable = radio_var) # The value field must be set in order to not trigger the two radios simultaneously
radio_1.pack()

radio_2 = ttk.Radiobutton(
    window,
    text = "Radiobutton 2",
    value = 2,
    variable = radio_var)
radio_2.pack() # With multiple radiobuttons only one will be true (namely active), with checkbuttons instead multiple of them can be active at the same time

radio_3 = ttk.Radiobutton(
    window,
    text = "Radiobutton 3",
    value = "Hello, I'm radiobutton 3.",
    variable = radio_var)
radio_3.pack()

frame = ttk.Frame(window)
radio_4 = ttk.Radiobutton(
    frame,
    text = "Radiobutton 4",
    value = 10,
    variable = radio_var)
radio_5 = ttk.Radiobutton(
    frame,
    text = "Radiobutton 5",
    value = 10,
    variable = radio_var)
radio_6 = ttk.Radiobutton(
    frame,
    text = "Radiobutton 6",
    value = 10,
    variable = radio_var)
button_3 = ttk.Button(
    window,
    text = "Press me to display radiobuttons' value.",
    command = button_2_func) # Since these last three radiobuttons have the same value, they will be triggered all at the same time
radio_4.pack()
radio_5.pack()
radio_6.pack()
button_3.pack()
frame.pack() # Also if inside a frame (thus with a different master), the radiobuttons are always all connected each other

# Data
check_bool = tk.BooleanVar()
radio_str = tk.StringVar()

# Widgets
check_AB = ttk.Checkbutton(
    window,
    text = "Checkbutton AB",
    command = lambda: print(radio_str.get()),
    variable = check_bool)
radio_A = ttk.Radiobutton(
    window,
    text = "Radiobutton A",
    value = "A",
    command = radio_func,
    variable = radio_str)
radio_B = ttk.Radiobutton(
    window,
    text = "Radiobutton B",
    value = "B",
    command = radio_func,
    variable = radio_str)

# Layout
check_AB.pack(pady = 10)
radio_A.pack()
radio_B.pack()

# Buttons with arguments
entry_str = tk.StringVar(value = "New test")
entry_3 = ttk.Entry(
    window,
    textvariable = entry_str) # I do not assign any text argument since it would be overwritten by the textvariable one
entry_3.pack(pady = 10)

button_4 = ttk.Button(
    window,
    text = "Button",
    command = lambda: button_4_func(entry_str)) # This lambda function tells Python to execute the function only when the button is pressed
button_4.pack()

# Run
window.mainloop()
