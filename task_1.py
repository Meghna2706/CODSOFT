from tkinter import *
from tkinter import messagebox

todo_items = [] # List to hold tasks

# Function to add a task
def add_item():
    task = entry_box.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "You must enter a task!")
    else:
        todo_items.append(task)
        update_list()
        entry_box.delete(0, END)

# Function to delete selected task
def remove_item():
    try:
        index = task_box.curselection()[0]
        todo_items.pop(index)
        update_list()
    except IndexError:
        messagebox.showerror("Error", "No task selected!")

# Function to refresh the listbox
def update_list():
    task_box.delete(0, END)
    for i, task in enumerate(todo_items, 1):
        task_box.insert(END, f"{i}. {task}")

# Main window setup
window = Tk()
window.title("To-Do List")
window.geometry("500x500")

# Heading
Label(window, text="Enter your to-do task", font=("Arial", 12, "bold")).pack(pady=10)

# Entry
entry_box = Entry(window, width=30)
entry_box.pack(pady=5)

# Buttons
Button(window, text="Add", width=10, command=add_item).pack(pady=5)

frame = Frame(window)
frame.pack(pady=10)

task_box = Listbox(frame, width=40, height=12)
task_box.pack(side=LEFT, fill=BOTH)

scroll = Scrollbar(frame, command=task_box.yview)
scroll.pack(side=RIGHT, fill=Y)

task_box.config(yscrollcommand=scroll.set)

# Delete and Exit buttons
Button(window, text="Delete", width=10, bg="red", fg="white", command=remove_item).pack(pady=5)
Button(window, text="Exit", width=10, command=window.quit).pack(pady=5)

window.mainloop()
