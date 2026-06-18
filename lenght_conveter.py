import tkinter as tk
from tkinter import ttk
def convert_length():
    try:
        inches = float(entry_input.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        label_result.config(text="Please enter a valid number")
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
label_title = tk.Label(root, text="Inches to Centimeters", font=("Arial", 16, "bold"))
label_title.pack(pady=20)
label_instruction = tk.Label(root, text="Enter value in Inches:", font=("Arial", 11))
label_instruction.pack(pady=5)
entry_input = tk.Entry(root, font=("Arial", 12), justify="center")
entry_input.pack(pady=5)
btn_convert = tk.Button(
    root,
    text="Convert",
    command=convert_length,
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
)
btn_convert.pack(pady=20)
label_result_heading = tk.Label(
    root, text="Result in Centimeters:", font=("Arial", 11)
)
label_result_heading.pack(pady=5)
label_result = tk.Label(root, text="0.00 cm", font=("Arial", 14, "bold"), fg="#2196F3")
label_result.pack(pady=5)
root.mainloop()