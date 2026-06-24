import tkinter as tk
import random
def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = f"Tie! Both chose {user_choice.capitalize()}."
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = f"You Win!\nComputer chose {computer_choice.capitalize()}."
    else:
        result = f"You Lose!\nComputer chose {computer_choice.capitalize()}."
    result_label.config(text=result)
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12))
instruction_label.pack(pady=30)
btn_rock = tk.Button(root, text="Rock", width=15, command=lambda: play("rock"))
btn_rock.pack(pady=10)
btn_paper = tk.Button(root, text="Paper", width=15, command=lambda: play("paper"))
btn_paper.pack(pady=10)
btn_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors"))
btn_scissors.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=30)
root.mainloop()
