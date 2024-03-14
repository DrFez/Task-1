import os
import csv



# What this file does:
# This file allows the admin to view, add, delete, and edit items in the items.csv file.

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
    
def print_prices():
    # Asks the user if they wish to view all items or items in a specific category
    choice = input("Do you want to view all items or items in a specific category?\n1. All items \n2. Specific category \n3. Exit \n")
    clear_terminal()
    if choice.lower() == '1':
        view_all_items()
    elif choice.lower() == '2':
        view_items_in_category()
    elif choice.lower() == '3':
        items_menu()
    else:
        print("\n\033[1mInvalid choice. Please enter '1' for All items or '2' for Specific category.\033[0m\n")
        print_prices()

def view_items_in_category():
    # Ask the user which category they want to view, whilst also printing all current categorys
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
        items_menu()
    clear_terminal()
    # Make chosen category the corospondent of the number chosen
    category = categories[int(category_number) - 1]


    #Prints the items in only that category with the same format as in view_all_items()
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

    # Print the headers "Items in category: " with the category being in bold
    print(f"Items in category: \033[1m{category}\033[0m\n")
    #Prints just the Item and Price 
    print("Item:".ljust(max_item_length + 1), "Price:")

    # Calculate the total length of the headers
    total_length = max_item_length + 8

    # Print dashes to create a separator
    print("-" * total_length)

    # Prints the items in the category and their prices. No color is used
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Category'] == category:
                item_name = row['Item']
                price = row['Price']
                print(f"{item_name.ljust(max_item_length + 1)}",
                    f"{price}")
            

            
def view_all_items():
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


    # Print category, item, and price with appropriate color
    for item in items:
        category = item[0]
        item_name = item[1]
        price = item[2]
        color = category_colors[category] 
        print(f"{color}{category.ljust(max_category_length + 1)}{RESET}",
            f"{item_name.ljust(max_item_length + 1)}",
            f"{price}{RESET}")


def navigate_to_primary_admin_script():
    # Get the path of the "Primary" directory relative to the current script's directory
    primary_path = os.path.join(os.path.dirname(__file__), "../Primary/admin.py")
    print(f"Primary path: {primary_path}")  # Debug print

    try:
        # Check if the primary admin script file exists
        if os.path.exists(primary_path):
            # Execute the primary admin script
            with open(primary_path) as file:
                code = file.read()
                exec(code)
        else:
            print("Primary admin script not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


def items_menu():
    while True:
        clear_terminal()
        print("Items Menu:")
        print("1. View items")
        print("2. Add item")
        print("3. Delete item")
        print("4. Edit item")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")
        
        clear_terminal()

        if choice == '1':
            view_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            delete()
        elif choice == '4':
            edit_item()
        elif choice == '5':
            navigate_to_primary_admin_script()
        else:
            print("\n\033[1mInvalid choice. Please enter a number from 1 to 5.\033[0m\n")



# A function that add items to the items.csv file
def add_new_item():
    # Get the category, item, and price from the user

    # Displays pre-existing categories that match letter. If the users input is different it will add the category to the list of categories
    categories = []
    file_path = os.path.join('CSV_Files', 'items.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            if category not in categories:
                categories.append(category)
                
    print("Categories: ", categories)

    category = input("Enter the category: ")

    if category == 'exit':
        items_menu()

    # Displays pre-existing items within that category. If new category is entered, it will not display any items
    items = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Category'] == category:
                item = row['Item']
                if item not in items:
                    items.append(item)
    print("Items: ", items)

    item = input("Enter the item: ")
    # Checks if the item already exists in the category
    if item == 'exit':
        items_menu()
    elif item in items:
        print("Item already exists in the category.")
        return
    else:
        price = input("Enter the price: ")

    # Append the data to the CSV file
    file_path = os.path.join('CSV_Files', 'items.csv')
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([category, item, price])

    print(f"Item '{item}' added successfully.")
    
# A function that can delete items from the items.csv file
def delete_item_or_category():
    choice = input("Do you want to delete an item or a category?\n1. Item \n2. Category \n3. Exit \n")
    clear_terminal()
    if choice.lower() == '1':
        item_to_delete = input("Enter the name of the item to delete: ")
        if item_to_delete == 'exit':
            items_menu()
        delete_item(item_to_delete)
    elif choice.lower() == '2':
        category_to_delete = input("Enter the name of the category to delete: ")
        if category_to_delete == 'exit':
            items_menu()
        delete_category(category_to_delete)
    elif choice.lower() == '3':
        items_menu()
    else:
        print("\n\033[1mInvalid choice. Please enter 'item' or 'category'.\033[0m\n")
        delete_item_or_category()


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
    
# A function that edits an item in the items.csv file (name or price)
def edit__exist_item():
    # Asks the user if they wish to search items first
    search = input("Do you want to search for an item first?\n1. Yes \n2. No \n3. Exit \n")
    clear_terminal()
    if search.lower() == '1':
        print_prices()
    elif search.lower() == '3':
        items_menu()

    # Get the item to edit from the user
    item_to_edit = input("Enter the name of the item to edit: ")
    if item_to_edit == 'exit':
        items_menu()
    # Ask if you want to edit the name or the price
    choice = input("Do you want to edit the name or the price?\n1. Name \n2. Price \n3. Exit \n")
    if choice.lower() == '1':
        new_name = input("Enter the new name: ")
        edit_item_name(item_to_edit, new_name)
    elif choice.lower() == '2':
        new_price = input("Enter the new price: ")
        edit_item_price(item_to_edit, new_price)
    elif choice.lower() == '3':
        items_menu()
    else:
        print("\n\033[1mInvalid choice. Please enter '1' for Name or '2' for Price.\033[0m\n")
        edit__exist_item()

def edit_item_name(old_name, new_name):
    file_path = os.path.join('CSV_Files', 'items.csv')
    temp_file_path = os.path.join('CSV_Files', 'temp.csv')

    # Check if the item exists in the CSV file
    item_exists = False

    with open(file_path, 'r', newline='') as csvfile, open(temp_file_path, 'w', newline='') as temp_csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(temp_csvfile)

        for row in reader:
            if row[1] == old_name:
                item_exists = True
                row[1] = new_name
            writer.writerow(row)

    # Replace the original file with the temporary file
    if item_exists:
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
        print(f"Item '{old_name}' edited successfully.")
    else:
        os.remove(temp_file_path)
        print(f"Item '{old_name}' not found in the file.")

def edit_item_price(item, new_price):
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
                row[2] = new_price
            writer.writerow(row)

    # Replace the original file with the temporary file
    if item_exists:
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
        print(f"Item '{item}' edited successfully.")
    else:
        os.remove(temp_file_path)
        print(f"Item '{item}' not found in the file.")

# Call respective functions based on user's choice
def view_items():
    clear_terminal()
    print_prices()
    while True:
        user_input = input("\nType '1' or click enter to return to the menu: ")
        sort_items()
        if user_input.lower() == '1' or user_input == '':
            break

def add_item():
    clear_terminal()
    add_new_item()
    while True:
        user_input = input("\nType '1' or click enter to return to the menu: ")
        sort_items()
        if user_input.lower() == '1' or user_input == '':
            break

def delete():
    clear_terminal()
    delete_item_or_category()
    while True:
        user_input = input("\nType '1' or click enter to return to the menu: ")
        sort_items()
        if user_input.lower() == '1' or user_input == '':
            break

def edit_item():
    clear_terminal()
    edit__exist_item()
    while True:
        user_input = input("\nType '1' or click enter to return to the menu: ")
        sort_items()
        if user_input.lower() == '1' or user_input == '':
            break


# Sorts the items in the items.csv file
sort_items()

# Clears the terminal screen
clear_terminal()

# Call the items_menu function to start
items_menu()


