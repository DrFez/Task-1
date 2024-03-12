import tkinter as tk
from tkinter import messagebox

# Dummy user credentials
valid_username = "admin"
valid_password = "123"

# Function to validate credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == valid_username and password == valid_password:
        root.destroy()
        #imports and runs main.py
        import main
        main

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login")

# Function to set focus on the username entry when the window is opened
def focus_username_entry(event):
    username_entry.focus_set()

# Set window size and position it in the center of the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Background color and font settings
bg_color = "#f0f0f0"
font_style = ("Arial", 12)

# Create a frame for the login form
login_frame = tk.Frame(root)
login_frame.pack(expand=True, padx=20, pady=20)

# Username label and entry
username_label = tk.Label(login_frame, text="Username:", font=font_style)
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame, font=font_style)
username_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.bind("<Return>", focus_username_entry)  # Pressing Enter moves focus to password entry

# Password label and entry
password_label = tk.Label(login_frame, text="Password:", font=font_style)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*", font=font_style)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(login_frame, text="Login", command=login, font=font_style, width=10)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Set focus on the username entry by default
username_entry.focus_set()

# Run the application
root.mainloop()
