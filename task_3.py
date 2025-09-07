'''To create a password generator'''

import random
import string
import tkinter as tk
from tkinter import messagebox

# Method to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Method to copy password
def copy_password():
    pwd = result_entry.get()
    if pwd:
        window.clipboard_clear()
        window.clipboard_append(pwd)
        window.update()
        messagebox.showinfo("Success","Password copied to clipboard")

# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(0,0)

# Label for length
l1=tk.Label(window, text="Enter Password Length:", font=("Times New Roman","12"))
l1.pack(pady=5)

# Entry for length
length_entry = tk.Entry(window, width=10, font=("Times New Roman","12"))
length_entry.pack(pady=5)

# Button to generate password
generate_btn = tk.Button(window, text="Generate Password", command=generate_password, bg="lightgreen", fg="black", font=("Times New Roman","12"))
generate_btn.pack(pady=5)

# Entry to show generated password
result_entry = tk.Entry(window, font=("Times New Roman","12"), width=30)
result_entry.pack(pady=5)

# Button to copy password
copy_btn = tk.Button(window, text="Copy to Clipboard", command=copy_password, bg="lightblue", fg="black", font=("Times New Roman","12"))
copy_btn.pack(pady=5)

# Run GUI
window.mainloop()

