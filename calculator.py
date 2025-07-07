#!/usr/bin/env python3

# Try different import methods for tkinter
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    try:
        import Tkinter as tk
        import tkMessageBox as messagebox
    except ImportError:
        print("Error: tkinter is not available. Please install tkinter.")
        print("For Arch Linux, run: sudo pacman -S tk")
        exit(1)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)

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
        # Replace common symbols for evaluation
        eval_expression = expression.replace('×', '*').replace('÷', '/')
        result = str(eval(eval_expression))
        expression_var.set(result)
        expression = result  # Keep result for further calculations
    except ZeroDivisionError:
        expression_var.set("Cannot divide by zero")
        expression = ""
    except Exception as e:
        expression_var.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression_var.set("")
    expression = ""

# Function to delete last character
def delete_last():
    global expression
    expression = expression[:-1]
    expression_var.set(expression)

# Create the display
display = tk.Entry(root, textvariable=expression_var, font=("Arial", 18), 
                  justify='right', state='readonly', bg='black', fg='white')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Configure grid weights
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Create buttons with better styling
button_style = {
    'width': 5, 
    'height': 2, 
    'font': ("Arial", 14),
    'relief': 'raised',
    'bd': 2
}

# Number and operator buttons
buttons = [
    ('C', 1, 0, '#ff6b6b', clear),
    ('⌫', 1, 1, '#4ecdc4', delete_last),
    ('÷', 1, 2, '#45b7d1', lambda: update_expression('÷')),
    ('×', 1, 3, '#45b7d1', lambda: update_expression('×')),
    
    ('7', 2, 0, '#f8f9fa', lambda: update_expression('7')),
    ('8', 2, 1, '#f8f9fa', lambda: update_expression('8')),
    ('9', 2, 2, '#f8f9fa', lambda: update_expression('9')),
    ('-', 2, 3, '#45b7d1', lambda: update_expression('-')),
    
    ('4', 3, 0, '#f8f9fa', lambda: update_expression('4')),
    ('5', 3, 1, '#f8f9fa', lambda: update_expression('5')),
    ('6', 3, 2, '#f8f9fa', lambda: update_expression('6')),
    ('+', 3, 3, '#45b7d1', lambda: update_expression('+')),
    
    ('1', 4, 0, '#f8f9fa', lambda: update_expression('1')),
    ('2', 4, 1, '#f8f9fa', lambda: update_expression('2')),
    ('3', 4, 2, '#f8f9fa', lambda: update_expression('3')),
    ('=', 4, 3, '#96ceb4', evaluate),
    
    ('0', 5, 0, '#f8f9fa', lambda: update_expression('0')),
    ('.', 5, 1, '#f8f9fa', lambda: update_expression('.')),
    ('(', 5, 2, '#45b7d1', lambda: update_expression('(')),
    (')', 5, 3, '#45b7d1', lambda: update_expression(')')),
]

# Create all buttons
for (text, row, col, color, command) in buttons:
    button = tk.Button(root, text=text, bg=color, fg='black' if color == '#f8f9fa' else 'white',
                      command=command, **button_style)
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Configure row weights for equal sizing
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Keyboard bindings
def on_key_press(event):
    key = event.char
    if key.isdigit():
        update_expression(key)
    elif key in '+-*/().':
        if key == '*':
            update_expression('×')
        elif key == '/':
            update_expression('÷')
        else:
            update_expression(key)
    elif key == '\r' or key == '=':  # Enter key
        evaluate()
    elif event.keysym == 'BackSpace':
        delete_last()
    elif event.keysym == 'Escape':
        clear()

root.bind('<Key>', on_key_press)
root.focus_set()  # Allow the window to receive key events

# Center the window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Start the main event loop
if __name__ == "__main__":
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nCalculator closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
