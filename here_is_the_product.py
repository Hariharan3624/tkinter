import tkinter as tk
from tkinter import messagebox

# Function to calculate the product
def calculate_product():
    try:
        # Retrieve numbers from entry widgets and convert to float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Calculate product
        product = num1 * num2
        
        # Clear the text box before inserting new result
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, f"{product}")
    except ValueError:
        # Display error message if input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

# Initialize the main window
window = tk.Tk()
window.title("getting started with widgets")
window.geometry("400x300")

# 1. Description Label
lbl_desc = tk.Label(
    window, 
    text="This application takes two numbers from the user,\ncalculates their product, and displays the result.",
    justify="center"
)
lbl_desc.pack(pady=10)

# 2. First Number Label and Entry
lbl_num1 = tk.Label(window, text="Enter the first number:")
lbl_num1.pack(pady=(5, 0))

entry_num1 = tk.Entry(window, width=20)
entry_num1.pack(pady=5)

# 3. Second Number Label and Entry
lbl_num2 = tk.Label(window, text="Enter the second number:")
lbl_num2.pack(pady=(5, 0))

entry_num2 = tk.Entry(window, width=20)
entry_num2.pack(pady=5)

# 4. Calculate Button
btn_calculate = tk.Button(window, text="Calculate Product", command=calculate_product)
btn_calculate.pack(pady=10)

# 5. Text Box for Result
text_result = tk.Text(window, width=25, height=1.5)
text_result.pack(pady=5)

# Run the application loop
window.mainloop()