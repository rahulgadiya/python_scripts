import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to store the expression
expression = ""
expression_var = tk.StringVar()

# Function to update the expression
def update_expression(value):
    global expression
    expression += str(value)
    expression_var.set(expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        expression_var.set(result)
        expression = ""
    except:
        expression_var.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression_var.set("")
    expression = ""

# Create the display
display = tk.Entry(root, textvariable=expression_var, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "%", "+"
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 14),
                       command=lambda value=button_text: update_expression(value))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the special buttons
equal_button = tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), command=evaluate)
equal_button.grid(row=5, column=3, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Start the main event loop
root.mainloop()
