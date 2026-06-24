import tkinter as tk
def check_strength(*args):
    password = password_entry.get()
    length = len(password)
    if length == 0:
        result_label.config(text="", bg="SystemButtonFace")
    elif length <= 5:
        result_label.config(text="Weak", fg="white", bg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="black", bg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="black", bg="lightgreen")
    else:
        result_label.config(text="Very Strong", fg="white", bg="darkgreen")
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
instruction_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
instruction_label.pack(pady=20)
password_var = tk.StringVar()
password_var.trace_add("write", check_strength)
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), show="*")
password_entry.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), width=15, height=2)
result_label.pack(pady=30)
root.mainloop()
