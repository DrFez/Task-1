
def edit_items_function():
    import edit_items_A
    edit_items_A.items_menu()

def receipts_function():
    import receipt_A
    receipt_A

def stock_function():
    import stock_A
    stock_A.stock_menu()

import tkinter as tk
from tkinter import messagebox



def admin_menu():


    def handle_choice(choice):
        if choice == '1':
            edit_items_function()
        elif choice == '2':
            receipts_function()
        elif choice == '3':
            stock_function()
        elif choice == '4':
            # Close the admin window
            root.destroy()
        else:
            messagebox.showerror("Invalid choice", "Please enter 1, 2, 3, or 4.")


    root = tk.Tk()
    root.title("Admin Menu")
    root.geometry("400x300")  # Set the window size

    # Bring the window to the front
    root.attributes('-topmost', 1)
    root.after_idle(root.attributes, '-topmost', 0)


    label = tk.Label(root, text="Admin Menu:", fg="purple", font=("Arial", 16))
    label.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    edit_items_button = tk.Button(button_frame, text="Edit Items", command=lambda: handle_choice('1'), font=("Arial", 14))
    edit_items_button.pack(pady=10)

    receipts_button = tk.Button(button_frame, text="Receipts", command=lambda: handle_choice('2'), font=("Arial", 14))
    receipts_button.pack(pady=10)

    stock_button = tk.Button(button_frame, text="Stock", command=lambda: handle_choice('3'), font=("Arial", 14))
    stock_button.pack(pady=10)

    exit_button = tk.Button(button_frame, text="Exit", command=lambda: handle_choice('4'), font=("Arial", 14))
    exit_button.pack(pady=10)

    root.mainloop()

admin_menu()

admin_menu()
