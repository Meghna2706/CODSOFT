"""Plays Rock, Paper, Scissors with loop in GUI."""
import random
import tkinter as tk
from tkinter import ttk, messagebox

# GUI
window = tk.Tk()
window.title("Rock, Paper, Scissor")
window.geometry("900x400")
window.resizable(0, 0)

# Global scores
user_score = 0
computer_score = 0

def sel(event=None):
    value = combo.get()

# Choices
options = ["rock", "paper", "scissor"]

# Combobox
combo = ttk.Combobox(window, values=options, font=("Times New Roman",12))
combo.bind("<<ComboboxSelected>>", sel)
combo.grid(column=2, row=2, padx=5, pady=5)
combo.current()

def messages(title, text):
    box = tk.Toplevel(window)
    box.title(title)
    box.geometry("300x300")
    box.resizable(0,0)

    # Center label
    msg_label = tk.Label(box, text=text, font=("Times New Roman", 12), justify="center")
    msg_label.pack(padx=20, pady=20)

    # OK button
    ok_btn = tk.Button(box, text=" OK ", command=box.destroy, bg="lightblue")
    ok_btn.pack(pady=10)

    box.grab_set()
    window.wait_window(box)

def play():
    global user_score, computer_score

    user_choice = combo.get()
    if user_choice not in options:
        messagebox.showwarning("Invalid", "Please select Rock, Paper, or Scissor!")
        return

    # Computer choice
    computer_choice = random.choice(options)
    computer_entry.delete(0, tk.END)
    computer_entry.insert(0, computer_choice)

    # Decide winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Combine everything in one message
    message = (
        f"You chose: {user_choice}\n"
        f"Computer chose: {computer_choice}\n\n"
        f"Result : {result}\n\n"
        f"Your Score: {user_score}\n"
        f"Computer Score: {computer_score}"
    )
    messages("Round Result", message)
    combo.set(" ")
    computer_entry.delete(0, tk.END)

def check_continue():
    global user_score, computer_score

    if continue_btn:
        # Final result
        if user_score > computer_score:
            final_msg = f" You won the game!\n\nFinal Scores\nYou: {user_score}\nComputer: {computer_score}"
        elif user_score < computer_score:
            final_msg = f" Computer won the game!\n\nFinal Scores\nYou: {user_score}\nComputer: {computer_score}"
        else:
            final_msg = f" The game ends in a tie!\n\nFinal Scores\nYou: {user_score}\nComputer: {computer_score}"
        messages("Game Over", final_msg)
        window.destroy()
    else:
        return

label_instruction=tk.Label(window, text="USER FRIENDLY ROCK, PAPER, AND SCISSORS GAME", font=("Times New Roman", 14, "underline"))
label_instruction.grid(row=1, column=2, pady=5)

# Label
user_label = tk.Label(window, text="Enter your choice (rock, paper, scissor):", font=("Times New Roman", 12))
user_label.grid(row=2, column=1, pady=5)

# Play Button
generate_btn = tk.Button(window, text="Play Round", command=play, bg="lightgreen", fg="black", font=("Times New Roman", 12))
generate_btn.grid(row=3, column=2, pady=5)

#label for computer's choice
computer_label = tk.Label(window, text="Computer's choice:", font=("Times New Roman", 12))
computer_label.grid(row=4, column=1, pady=5)

# Entry for computer choice
computer_entry = tk.Entry(window, width=30, font=("Times New Roman", 12))
computer_entry.grid(row=4, column=2, pady=5)

# Continue Button
continue_btn = tk.Button(window, text="End Game", command=check_continue, bg="lightpink", fg="black", font=("Times New Roman", 12))
continue_btn.grid(row=5, column=2, pady=5)

# Run GUI
window.mainloop()
