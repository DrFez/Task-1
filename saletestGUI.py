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
                if item_name.isalpha() and item_name.lower() == row[1].lower():
                    found = True
                    item_price = float(row[4])
                    items_listbox.insert(tk.END, f"{item_name} - {item_quantity} - ${item_price} - ${item_quantity * item_price}")
                    total_price += item_quantity * item_price
                    total_label.config(text=f"Total Price: ${total_price}")
                    break

            if not found:
                for row in reader:
                    if item_name in row[4]:
                        item = row
                        items_listbox.insert(tk.END, f"{item[1]} - {item_quantity} - ${item[4]} - ${item_quantity * float(item[4])}")
                        total_price += item_quantity * float(item[4])
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
            else:
                writer.writerow(["Payment: Card"])

        messagebox.showinfo("Success", f"Sale completed. Receipt saved as: {receipt_filename}")
        root.destroy()

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

    add_button = tk.Button(items_frame, text="Add Item", command=add_item)
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    items_listbox = tk.Listbox(items_frame, width=50, height=10)
    items_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    total_label = tk.Label(root, text=f"Total Price: ${total_price}")
    total_label.pack(pady=10)

    payment_var = tk.IntVar()
    payment_cash_radio = tk.Radiobutton(root, text="Cash", variable=payment_var, value=1)
    payment_cash_radio.pack()
    payment_card_radio = tk.Radiobutton(root, text="Card", variable=payment_var, value=2)
    payment_card_radio.pack()

    finish_button = tk.Button(root, text="Finish Sale", command=finish_sale)
    finish_button.pack(pady=10)

    root.mainloop()


# Call the process_sale function
process_sale()
