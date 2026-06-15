from datetime import date
import tkinter as tk
from tkinter import messagebox
def calculate_age():
    user_name = name_entry.get().strip()
    day_str = day_entry.get().strip()
    month_str = month_entry.get().strip()
    year_str = year_entry.get().strip()
    if not user_name or not day_str or not month_str or not year_str:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        birth_day = int(day_str)
        birth_month = int(month_str)
        birth_year = int(year_str)
        today = date.today()
        birth_date = date(birth_year, birth_month, birth_day)
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        result_label.config(
            text=f"Hello {user_name}!\nYou are {age} years old.", fg="#1b4332"
        )
    except ValueError:
        messagebox.showerror(
            "Error", "Please enter valid numbers for Date, Month, and Year."
        )
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.resizable(False, False) 
root.configure(bg="#f4f4f9")
header = tk.Label(
    root,
    text="Age Calculator",
    font=("Arial", 18, "bold"),
    bg="#f4f4f9",
    fg="#333333",
)
header.pack(pady=20)
input_frame = tk.Frame(root, bg="#f4f4f9")
input_frame.pack(pady=10)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=2)
label_opts = {"font": ("Arial", 11), "bg": "#f4f4f9", "anchor": "w"}
entry_opts = {"font": ("Arial", 11), "width": 18}
grid_opts = {"padx": 10, "pady": 8, "sticky": "w"}
tk.Label(input_frame, text="Name:", **label_opts).grid(
    row=0, column=0, **grid_opts
)
name_entry = tk.Entry(input_frame, **entry_opts)
name_entry.grid(row=0, column=1, **grid_opts)
tk.Label(input_frame, text="Birth Date (DD):", **label_opts).grid(
    row=1, column=0, **grid_opts
)
day_entry = tk.Entry(input_frame, **entry_opts)
day_entry.grid(row=1, column=1, **grid_opts)
tk.Label(input_frame, text="Birth Month (MM):", **label_opts).grid(
    row=2, column=0, **grid_opts
)
month_entry = tk.Entry(input_frame, **entry_opts)
month_entry.grid(row=2, column=1, **grid_opts)
tk.Label(input_frame, text="Birth Year (YYYY):", **label_opts).grid(
    row=3, column=0, **grid_opts
)
year_entry = tk.Entry(input_frame, **entry_opts)
year_entry.grid(row=3, column=1, **grid_opts)
calc_button = tk.Button(
    root,
    text="Calculate Age",
    font=("Arial", 11, "bold"),
    bg="#4a90e2",
    fg="white",
    command=calculate_age,
    padx=10,
    pady=5,
)
calc_button.pack(pady=20)
result_label = tk.Label(
    root, text="", font=("Arial", 13, "italic"), bg="#f4f4f9", justify="center"
)
result_label.pack(pady=10)
root.mainloop()