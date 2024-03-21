
def sale_function():
    import sale_GUI
    sale_GUI.process_sale()

def admin_function():
    import admin
    admin.admin_menu()

import tkinter as tk
from tkinter import messagebox

def main_menu():
    def handle_sale():
        sale_function()

    def handle_admin():
        admin_function()

    def handle_exit():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?\nThis will close the whole program.\nIncluding any other windows that are open."):
            root.destroy()
            # Close the entire program
            import sys
            sys.exit()

    # Create the main menu window

    root = tk.Tk()
    root.title("Main Menu")

    # Bring the window to the front
    root.attributes('-topmost', 1)
    root.after_idle(root.attributes, '-topmost', 0)


    # Make the window a fixed size and center it on the screen
    root.geometry("300x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')


    label = tk.Label(root, text="Main Menu:", font=("Arial", 16, "bold"))
    label.pack()

    button_sale = tk.Button(root, text="Sale", command=handle_sale, bg="green", fg="white", width=10, height=2)
    button_sale.pack(pady=10)

    button_admin = tk.Button(root, text="Admin", command=handle_admin, bg="purple", fg="white", width=10, height=2)
    button_admin.pack(pady=10)

    button_exit = tk.Button(root, text="Exit", command=handle_exit, bg="red", fg="white", width=10, height=2)
    button_exit.pack(pady=10)

    root.mainloop()

main_menu()
