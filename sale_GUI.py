import datetime
import os
import csv
import tkinter as tk
from tkinter import messagebox

# Function to process a sale
def process_sale():
    
    

    def add_item():
        nonlocal total_price
        item_name = item_entry.get()
        item_quantity = int(quantity_entry.get())
        found = False


        # Search for the item in the CSV file
        with open('CSV_Files/items.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if any(char.isalpha() for char in item_name):
                    if item_name.lower() == row[1].lower():
                        found = True
                        item_price = float(row[4])
                        # Check if item is already in the list
                        for i in range(items_listbox.size()):
                            item_info = items_listbox.get(i).split(" - ")
                            if item_info[0] == item_name:
                                # Update the quantity and total price
                                item_quantity += int(item_info[1])
                                total_price -= float(item_info[3][1:])
                                items_listbox.delete(i)
                                break
                        items_listbox.insert(tk.END, f"{item_name} - {item_quantity} - ${item_price} - ${item_quantity * item_price}")
                        total_price += item_quantity * item_price
                        total_label.config(text=f"Total Price: ${total_price}")
                        break
                # If input is numbers find the item by looking in the 4th (3) coloum of the csv file (Named Code) and set item to the row
                elif item_name.isdigit():
                    if item_name == row[4]:
                        found = True
                        item_price = float(row[4])
                        # Check if item is already in the list
                        for i in range(items_listbox.size()):
                            item_info = items_listbox.get(i).split(" - ")
                            if item_info[0] == row[1]:
                                # Update the quantity and total price
                                item_quantity += int(item_info[1])
                                total_price -= float(item_info[3][1:])
                                items_listbox.delete(i)
                                break
                        items_listbox.insert(tk.END, f"{row[1]} - {item_quantity} - ${item_price} - ${item_quantity * item_price}")
                        total_price += item_quantity * item_price
                        total_label.config(text=f"Total Price: ${total_price}")
                        break

            if not found:
                messagebox.showerror("Error", "Item not found in the inventory!")

    def finish_sale():
        receipt_filename = f"Receipts/{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"
        with open(receipt_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])  # Empty row for spacing
            writer.writerow(["Items"])
            writer.writerow(["Name", "Quantity", "Price", "Total Price"])
            for item in items_listbox.get(0, tk.END):
                item_info = item.split(" - ")
                writer.writerow([item_info[0], int(item_info[1]), float(item_info[2][1:]), float(item_info[3][1:])])
            gst = round(total_price * 0.1, 2)
            writer.writerow([])  # Empty row for spacing
            writer.writerow([f"GST: ${gst}"])
            writer.writerow([f"Total Price: ${total_price}"])
            if payment_var.get() == 1:
                writer.writerow(["Payment: Cash"])
            elif payment_var.get() == 2:
                writer.writerow(["Payment: Card"])
            else:
                # Shows error and forces the user to select cash or card
                messagebox.showerror("Error", "Please select a payment method!")
                return

        messagebox.showinfo("Success", f"Sale completed. Receipt saved as: {receipt_filename}")
        root.destroy()
        import main_menu
        main_menu.main_menu()




    def search():
        category = item_entry.get()
        # Create a new window for displaying the categories and items
        search_window = tk.Toplevel(root)
        search_window.title("Search Results")
        
        # Create a frame for the categories
        categories_frame = tk.Frame(search_window)
        categories_frame.pack(padx=10, pady=10)
        
        # Create a label for the categories
        categories_label = tk.Label(categories_frame, text="Categories:")
        categories_label.pack()
        
        # Create a listbox for displaying the categories
        categories_listbox = tk.Listbox(categories_frame, width=50, height=10)
        categories_listbox.pack()
        
        # Create a frame for the items
        items_frame = tk.Frame(search_window)
        items_frame.pack(padx=10, pady=10)
        
        # Create a label for the items
        items_label = tk.Label(items_frame, text="Items:")
        items_label.pack()
        
        # Create a listbox for displaying the items
        items_listbox = tk.Listbox(items_frame, width=50, height=10)
        items_listbox.pack()
        
        # Search for the categories in the CSV file
        with open('CSV_Files/items.csv', 'r') as file:
            reader = csv.reader(file)
            categories = set()
            for row in reader:
                categories.add(row[0])
        
        # Display the categories in the listbox
        for category in categories:
            if category != "Category":
                categories_listbox.insert(tk.END, category)
        
        def display_items():
            nonlocal items_listbox  # Add nonlocal statement
            selected_category = categories_listbox.get(categories_listbox.curselection())
            items_listbox.delete(0, tk.END)  # Clear the items listbox

            # Search for the items in the CSV file
            with open('CSV_Files/items.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if selected_category.lower() == row[0].lower():
                        items_listbox.insert(tk.END, f"Name: {row[1]} ({row[4]})")

            # When the user selects an item, write it to the input box for Item Name: on the main window
            def select_item(event):
                item_entry.delete(0, tk.END)
                selected_item = items_listbox.get(items_listbox.curselection())
                item_name = selected_item.split(": ")[1].split(" (")[0]
                item_entry.insert(0, item_name)
                search_window.destroy()

            # Bind the select_item function to the selection event of the items listbox
            items_listbox.bind("<<ListboxSelect>>", select_item)

        # Bind the display_items function to the selection event of the categories listbox
        categories_listbox.bind("<<ListboxSelect>>", lambda event: display_items())

        
    root = tk.Tk()
    root.title("Sales Processing")

    total_price = 0

    items_frame = tk.Frame(root)
    items_frame.pack(padx=10, pady=10)

    item_label = tk.Label(items_frame, text="Item Name:")
    item_label.grid(row=0, column=0, padx=5, pady=5)
    item_entry = tk.Entry(items_frame)
    item_entry.grid(row=0, column=1, padx=5, pady=5)

    quantity_label = tk.Label(items_frame, text="Quantity:")
    quantity_label.grid(row=1, column=0, padx=5, pady=5)
    quantity_entry = tk.Entry(items_frame)
    quantity_entry.grid(row=1, column=1, padx=5, pady=5)

    # Add item button
    add_button = tk.Button(items_frame, text="Add Item", command=add_item, bg="green", fg="white")
    add_button.grid(row=2, column=0, padx=5, pady=5)

    # A button to search for item by category
    search_button = tk.Button(items_frame, text="Search by category", command=search, bg="blue", fg="white")
    search_button.grid(row=2, column=1, padx=5, pady=5)

    # Center the buttons
    items_frame.grid_columnconfigure(0, weight=1)
    items_frame.grid_columnconfigure(1, weight=1)

    items_listbox = tk.Listbox(items_frame, width=50, height=10)
    items_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    total_label = tk.Label(root, text=f"Total Price: ${total_price}")
    total_label.pack(pady=10)

    payment_var = tk.IntVar()
    payment_cash_radio = tk.Radiobutton(root, text="Cash", variable=payment_var, value=1)
    payment_cash_radio.pack()
    payment_card_radio = tk.Radiobutton(root, text="Card", variable=payment_var, value=2)
    payment_card_radio.pack()

    finish_button = tk.Button(root, text="Finish Sale", command=finish_sale, bg="red", fg="white")
    finish_button.pack(pady=10)

    root.mainloop()


# Call the process_sale function
process_sale()
