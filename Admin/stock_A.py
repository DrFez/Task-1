# Manages the stock/inventory of the store.

import os
import csv

# ANSI escape codes for text colors
RESET = "\033[0m"
COLORS = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

# A function that clears the terminal screen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Puts the items in the items.csv file into alphabetical order
def sort_items():
    file_path = os.path.join('CSV_Files', 'items.csv')
    temp_file_path = os.path.join('CSV_Files', 'temp.csv')

    # Read the CSV file and store the data in a list
    items = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append((row['Category'], row['Item'], row['Price'], row['Stock']))

    # Sort the list of items
    items.sort()

    # Adds the headers to the top of the file
    with open(temp_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Item', 'Price', 'Stock'])
        for item in items:
            writer.writerow(item)

    # Write the sorted data to a temporary file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        with open(temp_file_path, newline='') as temp_csvfile:
            reader = csv.reader(temp_csvfile)
            for row in reader:
                writer.writerow(row)

    # Replace the original file with the temporary file
    os.remove(file_path)
    os.rename(temp_file_path, file_path)
    
# Edits the stock of an item in the items.csv file
def edit_stock(item_name, new_stock):
    file_path = os.path.join('CSV_Files', 'items.csv')
    temp_file_path = os.path.join('CSV_Files', 'temp.csv')

    # Read the CSV file and store the data in a list
    items = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append((row['Category'], row['Item'], row['Price'], row['Stock']))

    # Find the item to edit and change the stock
    found_item = False
    for i in range(len(items)):
        if items[i][1] == item_name:
            items[i] = (items[i][0], items[i][1], items[i][2], new_stock)
            found_item = True
            break

    if not found_item:
        print(f"Item '{item_name}' not found.")
        return

    # Adds the headers to the top of the file
    with open(temp_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Item', 'Price', 'Stock'])
        for item in items:
            writer.writerow(item)

    # Write the edited data to a temporary file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        with open(temp_file_path, newline='') as temp_csvfile:
            reader = csv.reader(temp_csvfile)
            for row in reader:
                writer.writerow(row)

    # Replace the original file with the temporary file
    os.remove(file_path)
    os.rename(temp_file_path, file_path)

    print(f"Stock for item '{item_name}' has been updated to '{new_stock}'.")

def view_items_in_category():
    # Ask the user which category they want to view, whilst also printing all current categories
    categories = []
    file_path = os.path.join('CSV_Files', 'items.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            if category not in categories:
                categories.append(category)
    # Prints the categories in the items.csv file in a list with the format N. Category on the same line
    print("Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    # Asks the user to input the number of the category they want to view
    category_number = input("Enter the number of the category you want to view: ")
    if category_number == 'exit':
        menu()
    clear_terminal()
    # Make chosen category the correspondent of the number chosen
    category = categories[int(category_number) - 1]


    # Prints the items in only that category with the format Category, Item, Stock
    file_path = os.path.join('CSV_Files', 'items.csv')
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Initialize variables to store maximum lengths
    max_category_length = 0
    max_item_length = 0

    # Read the CSV file to find the maximum lengths
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category_length = len(row['Category'])
            item_length = len(row['Item'])
            max_category_length = max(max_category_length, category_length)
            max_item_length = max(max_item_length, item_length)

    # Print the headers "Category, Item, Stock"
    print("Category:".ljust(max_category_length + 1), "Item:".ljust(max_item_length + 1), "Stock:")

    # Calculate the total length of the headers
    total_length = max_category_length + max_item_length + 8

    # Print dashes to create a separator
    print("-" * total_length)

    # Prints the items in the category and their stock
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Category'] == category:
                category_name = row['Category']
                item_name = row['Item']
                stock = row['Stock']
                print(f"{category_name.ljust(max_category_length + 1)}",
                    f"{item_name.ljust(max_item_length + 1)}",
                    f"     {stock}")

# Prints the stock using same format as edit_items_A from the items.csv file (Category, Item, Stock)
def print_all_stock():
    file_path = os.path.join('CSV_Files', 'items.csv')
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Initialize variables to store maximum lengths
    max_category_length = 0
    max_item_length = 0

    # Read the CSV file to find the maximum lengths
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category_length = len(row['Category'])
            item_length = len(row['Item'])
            max_category_length = max(max_category_length, category_length)
            max_item_length = max(max_item_length, item_length)
    
    # Print the headers
    print("Category:".ljust(max_category_length + 1), "Item:".ljust(max_item_length + 1), "Stock:")

    # Calculate the total length of the headers
    total_length = max_category_length + max_item_length + 15

    # Print dashes to create a separator
    print("-" * total_length)

    # Read the CSV file again to print the data
    category_colors = {}
    color_index = 0
    items = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            item = row['Item']
            stock = row['Stock']

            # Determine color for the category
            if category not in category_colors:
                category_colors[category] = COLORS[color_index % len(COLORS)]
                color_index += 1
            color = category_colors[category]

            # Add item to the list
            items.append((category, item, stock))


    # Print category, item, and stock
    for item in items:
        category = item[0]
        item_name = item[1]
        stock = item[2]
        color = category_colors[category] 
        print(f"{color}{category.ljust(max_category_length + 1)}{RESET}",
            f"{item_name.ljust(max_item_length + 1)}",
            f"     {stock}{RESET}")

# Ask the user if they to view all stock or stock in a specific category
def print_stock():
    while True:
        print("Stock Management:")
        print("1. View All Stock")
        print("2. View Stock in a Specific Category")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        clear_terminal()
        if choice == '1':
            print_all_stock()
            break
        elif choice == '2':
            view_items_in_category()
            break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Function Menu (View Stock, Manage Stock, Exit)
def menu():
    while True:
        
        print("Stock Management Menu:")
        print("1. View Stock")
        print("2. Manage Stock")
        print("3. Exit")

        choice = input("Enter your choice: ")
        clear_terminal()
        if choice == "1":
            view_stock()
        elif choice == "2":
            manage_stock()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def view_stock():
    clear_terminal()
    print_stock()
    while True:
        user_input = input("\nType '1' or click enter to return to the menu or enter an item name to edit its stock: ")
        clear_terminal()
        sort_items()
        if user_input.lower() == '1' or user_input == '':
            break
        else: 
            edit_stock_name = user_input
            edit_stock_amount = input("Enter the new stock amount: ")
            # Calls the edit_stock function with the item name and new stock amount as arguments
            edit_stock(edit_stock_name, edit_stock_amount)

def manage_stock():
    clear_terminal()
    #Ask the user if they want to view all items first through input
    view_all_items = input("Do you want to view items first?\n1. Yes \n2. No\n3. Exit\nEnter your choice: ")
    if view_all_items.lower() == '1':
        print_all_stock()
    elif view_all_items.lower() == '3':
        clear_terminal()
        menu()
    
    # Asks the user if they want to change the stock of a single item or multiple items
    while True:
        clear_terminal()
        print("Do you want to edit the stock of a single item or multiple items?")
        print("1. Single Item")
        print("2. Multiple Items")
        print("3. Exit")
        choice = input("Enter your choice: ")
        clear_terminal()
        if choice == "2":
            # Asks for the name of the items in the format "Item1 Stock, Item2 Stock, Item3 Stock, etc."
            items = input("Enter the name of the items you want to edit and their new stock amount in the format 'Item1 Stock, Item2 Stock, Item3 Stock, etc.': ")
            # Runs edit_stock for each item in the list
            for item in items.split(", "):
                item_name, stock = item.split(" ")
                edit_stock(item_name, stock)
            break
        # Elif choice is not 1 2 or 3, print invalid choice and ask again
        elif choice != "1" and choice != "2" and choice != "3":
            print("Invalid choice. Please try again.")
        else:
            edit_stock_name = input("Enter the name of the item you want to edit: ")
            edit_stock_amount = input("Enter the new stock amount: ")
            # Calls the edit_stock function with the item name and new stock amount as arguments
            edit_stock(edit_stock_name, edit_stock_amount)
            while True:
                user_input = input("\nType '1' or click enter to return to the menu: ")
                clear_terminal()
                sort_items()
                if user_input.lower() == '1' or user_input == '':
                    break

sort_items()
menu()


