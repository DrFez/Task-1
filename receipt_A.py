import datetime
import os
import time
import csv
import subprocess
import platform


# This function clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# This function asks if they want a sale receipt or a stock receipt
def receipt_menu():
    while True:
        clear_terminal()
        print("\033[1m" + "Receipt Menu:")
        print("\033[0m" + "1. Sale Receipt")
        print("2. Stock Receipt")
        print("3. Delete Receipts")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3): ")
        clear_terminal()
        clear_terminal()
        if choice == '1':
            sale_receipt()
            break
        elif choice == '2':
            stock_receipt()
            break
        elif choice == '3':
            delete_receipts()
            break
        elif choice == '3':
            import admin
            admin.admin_menu()
            break
        elif choice == '4':
            import main_menu
            main_menu.main_menu()
        else:
            print("\033[1m" + "Invalid choice. Please enter 1, 2, or 3.")
            print("\033[0m" + """""")

def sale_receipt():
    # Open the Finder/Explorer window to the "Receipts" folder
    if platform.system() == 'Windows':
        subprocess.Popen(['explorer', 'Receipts'])
    elif platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', 'Receipts'])
    elif platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', 'Receipts'])
    else:
        print("Unsupported platform")


def delete_receipts():
    # Open the Finder/Explorer window to the "Exports" folder
    if platform.system() == 'Windows':
        subprocess.Popen(['explorer', 'Exports'])
    elif platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', 'Exports'])
    elif platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', 'Exports'])
    else:
        print("Unsupported platform")

    # Wait for 2 seconds
    time.sleep(2)
    # Assuming receipt_menu() is defined elsewhere in your code
    receipt_menu()


def stock_receipt():
    # Asks if they want to export the stock to a csv file or txt file
    while True:
        import stock_A
        stock_A.print_stock()
        print("\n\033[1m" + "Stock Receipt:")
        print("\033[0m" + "1. Export to CSV")
        print("2. Export to TXT")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        clear_terminal()
        if choice == '1':
            export_stock_to_csv()
            break
        elif choice == '2':
            export_stock_to_txt()
            break
        elif choice == '3':
            receipt_menu()
            break
        else:
            print("\033[1m" + "Invalid choice. Please enter 1, 2, or 3.")
            print("\033[0m" + """""")

# This function exports the stock to a csv file
def export_stock_to_csv():
    import stock_A
    
    # If amount is "all" then export all stock
    if stock_A.amount_printed == "all":
        # Create the directory "Exports" if it doesn't exist
        if not os.path.exists('Exports'):
            os.makedirs('Exports')
        # Create the directory "csv" if it doesn't exist
        if not os.path.exists('Exports/csv'):
            os.makedirs('Exports/csv')
        # Create a new CSV file in the folder "csv" located in the folder "Exports". Name the file "AllStock-date-time.csv"
        with open(f'Exports/csv/AllStock-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv', 'w', newline='') as file:
            file_path = os.path.join('CSV_Files', 'items.csv')
            export_file_path = os.path.join('Exports', 'csv', f'AllStock-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv')

            # Read the CSV file and store the data in a list
            items = []
        
            # Create the CSV with it just being: Category, Item, Stock
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    items.append([row['Category'], row['Item'], row['Stock']])
            
            # Add a header to the CSV file
            items.insert(0, ['Category', 'Item', 'Stock'])

            # Write the data to the export file
            with open(export_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(items)
            


            # Export successful in bold and green and underlined
            clear_terminal()
            print("\033[1m" + "\033[32m" + "\033[4m" + "Export successful" + "\033[0m")
            
            # Wait for 2 seconds
            time.sleep(2)
            receipt_menu()
    else:
        # Make catergory var stock_A.amount_printed
        category = stock_A.amount_printed
        # Create the directory "Exports" if it doesn't exist
        if not os.path.exists('Exports'):
            os.makedirs('Exports')
        # Create the directory "csv" if it doesn't exist
        if not os.path.exists('Exports/csv'):
            os.makedirs('Exports/csv')
        # Create a new CSV file in the folder "csv" located in the folder "Exports". Name the file "{Category}-date-time.csv"
        with open(f'Exports/csv/{category}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv', 'w', newline='') as file:
            file_path = os.path.join('CSV_Files', 'items.csv')
            export_file_path = os.path.join('Exports', 'csv', f'{category}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv')

            # Read the CSV file and store the data in a list
            items = []
        
            # Create the CSV with it just being: Item, Stock
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Category'] == category:
                        items.append([row['Item'], row['Stock']])
            
            # Add a header to the CSV file
            items.insert(0, ['Item', 'Stock'])

            # Write the data to the export file
            with open(export_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(items)
            

            # Export successful in bold and green and underlined
            clear_terminal()
            print("\033[1m" + "\033[32m" + "\033[4m" + "Export successful" + "\033[0m")
            
            # Wait for 2 seconds
            time.sleep(2)
            receipt_menu()
    
            
# This function exports the stock to a txt file
def export_stock_to_txt():
    import stock_A

    # If amount is "all" then export all stock
    if stock_A.amount_printed == "all":
        # Create the directory "Exports" if it doesn't exist
        if not os.path.exists('Exports'):
            os.makedirs('Exports')
        # Create the directory "txt" if it doesn't exist
        if not os.path.exists('Exports/txt'):
            os.makedirs('Exports/txt')
        # Create a new TXT file in the folder "txt" located in the folder "Exports". Name the file "AllStock-date-time.txt"
        with open(f'Exports/txt/AllStock-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt', 'w') as file:
            file_path = os.path.join('CSV_Files', 'items.csv')
            export_file_path = os.path.join('Exports', 'txt', f'AllStock-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt')

            # Read the CSV file and store the data in a list
            items = []
        
            # Dictionary to store items grouped by category
            category_items = {}

            # Read the CSV file and populate the dictionary
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category = row['Category']
                    item = row['Item']
                    stock = row['Stock']
                    # Check if category exists in the dictionary
                    if category in category_items:
                        category_items[category].append((item, stock))
                    else:
                        category_items[category] = [(item, stock)]

            # Write the data to the export file grouped by category
            with open(export_file_path, 'w') as file:
                for category, items in category_items.items():
                    # Write the category to the file
                    file.write(f"Category: {category}\n")
                    # Write all items in that category
                    for item, stock in items:
                        file.write(f"{item}: {stock}\n")
                    # Add a newline to separate categories
                    file.write("\n")
                

            
            # Export successful in bold and green and underlined
            clear_terminal()
            print("\033[1m" + "\033[32m" + "\033[4m" + "Export successful" + "\033[0m")
            
            # Wait for 2 seconds
            time.sleep(2)
            receipt_menu()
    else:
        # Make catergory var stock_A.amount_printed
        category = stock_A.amount_printed
        # Create the directory "Exports" if it doesn't exist
        if not os.path.exists('Exports'):
            os.makedirs('Exports')
        # Create the directory "txt" if it doesn't exist
        if not os.path.exists('Exports/txt'):
            os.makedirs('Exports/txt')
        # Create a new TXT file in the folder "txt" located in the folder "Exports". Name the file "{Category}-date-time.txt"
        with open(f'Exports/txt/{category}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt', 'w') as file:
            file_path = os.path.join('CSV_Files', 'items.csv')
            export_file_path = os.path.join('Exports', 'txt', f'{category}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt')

            # Read the CSV file and store the data in a list
            items = []
        
            # Create the CSV with it just being: Item, Stock
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Category'] == category:
                        items.append([row['Item'], row['Stock']])
                               
            
            # Write the data to the export file Item: {Item} - Stock: {Stock}
            with open(export_file_path, 'w') as file:
                for item, stock in items:
                    file.write(f"Item: {item} - Stock: {stock}\n")
            
            

            # Export successful in bold and green and underlined
            clear_terminal()
            print("\033[1m" + "\033[32m" + "\033[4m" + "Export successful" + "\033[0m")
            
            # Wait for 2 seconds
            time.sleep(2)


receipt_menu()