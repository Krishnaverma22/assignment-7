import tkinter as tk

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Cannot divide by zero")
                return
        else:
            result_label.config(text="Invalid operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create and place the input labels and entry fields
num1_label = tk.Label(window, text="Number 1:")
num1_label.grid(row=0, column=0)
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(window, text="Number 2:")
num2_label.grid(row=1, column=0)
num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1)

# Create and place the operation radio buttons
operation_var = tk.StringVar()
operation_var.set("Addition")

addition_radio = tk.Radiobutton(window, text="Addition", variable=operation_var, value="Addition")
addition_radio.grid(row=2, column=0)
subtraction_radio = tk.Radiobutton(window, text="Subtraction", variable=operation_var, value="Subtraction")
subtraction_radio.grid(row=2, column=1)
multiplication_radio = tk.Radiobutton(window, text="Multiplication", variable=operation_var, value="Multiplication")
multiplication_radio.grid(row=3, column=0)
division_radio = tk.Radiobutton(window, text="Division", variable=operation_var, value="Division")
division_radio.grid(row=3, column=1)

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, columnspan=2)

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.grid(row=5, columnspan=2)

# Start the main event loop
window.mainloop()
