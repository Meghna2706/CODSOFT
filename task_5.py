from tkinter import *
from tkinter import messagebox
import os

# save in file
CONTACT_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    contacts.append(parts)
    return contacts

def save_contacts():
    with open(CONTACT_FILE, "w") as f:
        for c in contactlist:
            f.write(" | ".join(c) + "\n")

window = Tk()
window.title("Contact Book")
window.geometry("500x400")
window.resizable(False, False)

contactlist = load_contacts()

# Variables
Name = StringVar()
Number = StringVar()
Email = StringVar()
Address = StringVar()
Search = StringVar()

def refresh_list(filtered=None):
    contact_box.delete(0, END)
    display = filtered if filtered is not None else contactlist
    for i, (n, p, e, a) in enumerate(display, start=1):
        contact_box.insert(END, f"{i}. {n}")

def reset_entries():
    Name.set("")
    Number.set("")
    Email.set("")
    Address.set("")
    Search.set("")

def add_contact():
    if Name.get() and Number.get() and Email.get() and Address.get():
        contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
        save_contacts()
        refresh_list()
        reset_entries()
        messagebox.showinfo("Added", "Contact added successfully")
    else:
        messagebox.showwarning("Warning", "Please fill all fields")

def update_contact():
    selected = contact_box.curselection()
    if selected:
        idx = selected[0]
        contactlist[idx] = [Name.get(), Number.get(), Email.get(), Address.get()]
        save_contacts()
        refresh_list()
        reset_entries()
        messagebox.showinfo("Updated", "Contact updated successfully")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update")

def delete_contact():
    selected = contact_box.curselection()
    if selected:
        idx = selected[0]
        contactlist.pop(idx)
        save_contacts()
        refresh_list()
        reset_entries()
        messagebox.showinfo("Deleted", "Contact deleted successfully")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete")

def on_select(event):
    selected = contact_box.curselection()
    if selected:
        idx = selected[0]
        n, p, e, a = contactlist[idx]
        Name.set(n)
        Number.set(p)
        Email.set(e)
        Address.set(a)

def search_contact():
    term = Search.get().strip().lower()
    if term:
        filtered = [c for c in contactlist if term in c[0].lower()]
        refresh_list(filtered)
    else:
        refresh_list()

def exit_app():
    save_contacts()
    window.destroy()

label_frame = Frame(window, padx=10, pady=10)
label_frame.pack(fill=X)

Label(label_frame, text="Name:").grid(row=0, column=0, pady=5)
Entry(label_frame, textvariable=Name, width=35).grid(row=0, column=1, pady=5)

Label(label_frame, text="Contact No.:").grid(row=1, column=0, pady=5)
Entry(label_frame, textvariable=Number, width=35).grid(row=1, column=1, pady=5)

Label(label_frame, text="Email:").grid(row=2, column=0, pady=5)
Entry(label_frame, textvariable=Email, width=35).grid(row=2, column=1, pady=5)

Label(label_frame, text="Address:").grid(row=3, column=0, pady=5)
Entry(label_frame, textvariable=Address, width=35).grid(row=3, column=1, pady=5)

# Search box
Label(label_frame, text="Search:").grid(row=4, column=0, pady=5)
Entry(label_frame, textvariable=Search, width=35).grid(row=4, column=1, pady=5)
Button(label_frame, text="Search", bg="yellow", command=search_contact).grid(row=4, column=2, padx=5, pady=5)

# Buttons
btn_frame = Frame(window, pady=10)
btn_frame.pack()

Button(btn_frame, text="Add", width=10, bg="lightblue", command=add_contact).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Update", width=10, bg="lightblue", command=update_contact).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Delete", width=10, bg="lightblue", command=delete_contact).grid(row=0, column=2, padx=5)
Button(btn_frame, text="Reset", width=10, bg="lightblue", command=reset_entries).grid(row=0, column=3, padx=5)
Button(btn_frame, text="Exit", width=10, bg="red", fg="white", command=exit_app).grid(row=0, column=4, padx=5)

# Contact List
list_frame = Frame(window, padx=10, pady=30)
list_frame.pack()

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

contact_box = Listbox(list_frame, height=12, width=60, yscrollcommand=scrollbar.set, font=("Times New Roman", 13))
contact_box.pack(side=LEFT)
scrollbar.config(command=contact_box.yview)

contact_box.bind("<<ListboxSelect>>", on_select)

refresh_list()
window.mainloop()
