import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())
        simple_interest = (p * t * r) / 100
        compound_interest = p * ((1 + r / 100) ** t) - p
        lbl_si_val.config(text=f"${simple_interest:,.2f}")
        lbl_ci_val.config(text=f"$ {compound_interest:,.2f}")
    except ValueError:
        messagebox.onerror(
            "Input Error", "Please enter valid numeric values for all fields."
        )
root = tk.Tk()
root.title("Age Calculator App") 
root.geometry("400x400")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
lbl_header = tk.Label(
    root, text="Interest Calculator", font=("Arial", 16, "bold"), pady=10
)
lbl_header.grid(row=0, column=0, columnspan=2, pady=(10, 20))
lbl_principal = tk.Label(root, text="Principal Amount:", font=("Arial", 11))
lbl_principal.grid(row=1, column=0, sticky="e", padx=10, pady=8)
entry_principal = tk.Entry(root, font=("Arial", 11), width=15)
entry_principal.grid(row=1, column=1, sticky="w", padx=10, pady=8)
lbl_time = tk.Label(root, text="Time (Years):", font=("Arial", 11))
lbl_time.grid(row=2, column=0, sticky="e", padx=10, pady=8)
entry_time = tk.Entry(root, font=("Arial", 11), width=15)
entry_time.grid(row=2, column=1, sticky="w", padx=10, pady=8)
lbl_rate = tk.Label(root, text="Rate of Interest (%):", font=("Arial", 11))
lbl_rate.grid(row=3, column=0, sticky="e", padx=10, pady=8)
entry_rate = tk.Entry(root, font=("Arial", 11), width=15)
entry_rate.grid(row=3, column=1, sticky="w", padx=10, pady=8)
btn_calculate = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate_interest,
    padx=10,
    pady=5,
)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=20)
lbl_si_text = tk.Label(
    root, text="Simple Interest:", font=("Arial", 11, "bold")
)
lbl_si_text.grid(row=5, column=0, sticky="e", padx=10, pady=6)
lbl_si_val = tk.Label(
    root, text="₹ 0.00", font=("Arial", 11, "bold"), fg="#2196F3"
)
lbl_si_val.grid(row=5, column=1, sticky="w", padx=10, pady=6)
lbl_ci_text = tk.Label(
    root, text="Compound Interest:", font=("Arial", 11, "bold")
)
lbl_ci_text.grid(row=6, column=0, sticky="e", padx=10, pady=6)
lbl_ci_val = tk.Label(
    root, text="₹ 0.00", font=("Arial", 11, "bold"), fg="#9C27B0"
)
lbl_ci_val.grid(row=6, column=1, sticky="w", padx=10, pady=6)
root.mainloop()