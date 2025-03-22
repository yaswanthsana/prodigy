import tkinter as tk
from tkinter import messagebox, simpledialog
import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = load_contacts()
        
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="View Contacts", command=self.view_contacts).pack(pady=5)
        tk.Button(root, text="Edit Contact", command=self.edit_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        
        self.contacts[name] = {"phone": phone, "email": email}
        save_contacts(self.contacts)
        messagebox.showinfo("Success", "Contact added successfully!")
    
    def view_contacts(self):
        contact_list = "".join([f"{name}: {data['phone']} | {data['email']}\n" for name, data in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list if contact_list else "No contacts found.")
    
    def edit_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to edit:")
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return
        
        phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
        email = simpledialog.askstring("Input", "Enter new email address:", initialvalue=self.contacts[name]["email"])
        
        self.contacts[name] = {"phone": phone, "email": email}
        save_contacts(self.contacts)
        messagebox.showinfo("Success", "Contact updated successfully!")
    
    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            save_contacts(self.contacts)
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
