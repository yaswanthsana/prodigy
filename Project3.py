import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email Address:")

    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")

# View all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']} - {info['email']}")

# Edit a contact
def edit_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected")
        return
    name = contact_list.get(selected[0]).split(' - ')[0]
    phone = simpledialog.askstring("Input", f"Enter new phone number for {name}:", initialvalue=contacts[name]["phone"])
    email = simpledialog.askstring("Input", f"Enter new email for {name}:", initialvalue=contacts[name]["email"])
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    refresh_contact_list()
    messagebox.showinfo("Success", "Contact updated successfully!")

# Delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected")
        return
    name = contact_list.get(selected[0]).split(' - ')[0]
    if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?"):
        del contacts[name]
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Deleted", f"{name} deleted successfully!")

# Refresh contact list
def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']} - {info['email']}")

# Main application window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x400")

# Load contacts initially
contacts = load_contacts()

# Create GUI Elements
frame = tk.Frame(root)
frame.pack(pady=10)

contact_list = tk.Listbox(frame, width=60, height=15)
contact_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_list.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(btn_frame, text="Edit Contact", command=edit_contact)
btn_edit.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=0, column=2, padx=5)

btn_view = tk.Button(btn_frame, text="View Contacts", command=view_contacts)
btn_view.grid(row=0, column=3, padx=5)

# Initialize contact list
refresh_contact_list()

# Start GUI
root.mainloop()
