import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if the user exists in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

    # Close the connection
    conn.close()

# Function to clear the input fields
def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username Label and Entry
tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login and Clear Buttons
tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
