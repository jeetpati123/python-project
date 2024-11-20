import tkinter as tk
from tkinter import ttk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create the main application window
root = tk.Tk()
root.title("Responsive Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Entry widget for displaying and input
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.pack(padx=10, pady=10, fill="x")

# Create the button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_frame = ttk.Frame(root)
button_frame.pack(fill="both", expand=True)

# Add buttons dynamically to the grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        button = ttk.Button(button_frame, text=btn_text, style="TButton")
        button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
        button.bind("<Button-1>", on_button_click)

# Make the grid cells equally sized
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Run the main application loop
root.mainloop()
