import os
import csv

# ANSI escape codes for text colors
RESET = "\033[0m"
COLORS = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]


def print_prices():
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
    print("Category:".ljust(max_category_length + 1), "Item:".ljust(max_item_length + 1), "Price:")
    
    # Calculate the total length of the headers
    total_length = max_category_length + max_item_length + 10

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
            price = row['Price']

            # Determine color for the category
            if category not in category_colors:
                category_colors[category] = COLORS[color_index % len(COLORS)]
                color_index += 1
            color = category_colors[category]

            # Add item to the list
            items.append((category, item, price))

    # Sort items by category and then by item name
    items.sort(key=lambda x: (x[0], x[1]))

    # Print category, item, and price with appropriate color
    for item in items:
        category = item[0]
        item_name = item[1]
        price = item[2]
        color = category_colors[category] 
        print(f"{color}{category.ljust(max_category_length + 1)}{RESET}",
            f"{item_name.ljust(max_item_length + 1)}",
            f"{price}{RESET}")


def items_menu():
    while True:
        print("\nItems Menu:")
        print("1. View items")
        print("2. Add item")
        print("3. Delete item")
        print("4. Edit item")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            view_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            delete()
        elif choice == '4':
            edit_item()
        elif choice == '5':
            print("Exiting items menu.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# A function that add items to the items.csv file
def add_new_item():
    # Get the category, item, and price from the user
    category = input("Enter the category: ")
    item = input("Enter the item: ")
    price = input("Enter the price: ")

    # Append the data to the CSV file
    file_path = os.path.join('CSV_Files', 'items.csv')
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([category, item, price])

    print(f"Item '{item}' added successfully.")
    
# A function that can delete items from the items.csv file
def delete_item_or_category():
    choice = input("Do you want to delete an item or a category? (item/category): ")
    if choice.lower() == 'item':
        item_to_delete = input("Enter the name of the item to delete: ")
        delete_item(item_to_delete)
    elif choice.lower() == 'category':
        category_to_delete = input("Enter the name of the category to delete: ")
        delete_category(category_to_delete)
    else:
        print("Invalid choice. Please enter 'item' or 'category'.")


# A function that deletes a category from the items.csv file
def delete_category(category):
    file_path = os.path.join('CSV_Files', 'items.csv')
    temp_file_path = os.path.join('CSV_Files', 'temp.csv')

    # Check if the category exists in the CSV file
    category_exists = False

    with open(file_path, 'r', newline='') as csvfile, open(temp_file_path, 'w', newline='') as temp_csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(temp_csvfile)

        for row in reader:
            if row[0] == category:
                category_exists = True
            else:
                writer.writerow(row)

    # Replace the original file with the temporary file
    if category_exists:
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
        print(f"Category '{category}' deleted successfully.")
    else:
        os.remove(temp_file_path)
        print(f"Category '{category}' not found in the file.")
     
# A function that deletes an item from the items.csv file
def delete_item(item):
    file_path = os.path.join('CSV_Files', 'items.csv')
    temp_file_path = os.path.join('CSV_Files', 'temp.csv')

    # Check if the item exists in the CSV file
    item_exists = False

    with open(file_path, 'r', newline='') as csvfile, open(temp_file_path, 'w', newline='') as temp_csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(temp_csvfile)

        for row in reader:
            if row[1] == item:
                item_exists = True
            else:
                writer.writerow(row)

    # Replace the original file with the temporary file
    if item_exists:
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
        print(f"Item '{item}' deleted successfully.")
    else:
        os.remove(temp_file_path)
        print(f"Item '{item}' not found in the file.")

# Call respective functions based on user's choice
def view_items():
    print_prices()
    while True:
        user_input = input("Type 'exit' to return to the menu: ")
        if user_input.lower() == 'exit':
            break

def add_item():
    add_new_item()
    while True:
        user_input = input("Type 'exit' to return to the menu: ")
        if user_input.lower() == 'exit':
            break

def delete():
    delete_item_or_category()
    while True:
        user_input = input("Type 'exit' to return to the menu: ")
        if user_input.lower() == 'exit':
            break

def edit_item():
    print("Editing item...")


# Call the items_menu function to start
items_menu()

