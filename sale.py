# Processes Sales
import datetime
import os
import sys
import time
import csv

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the total price
OutFun_total_price = 0

# Initialize the list of items
OutFun_items = []

# Initialize the list of quantities
OutFun_quantities = []

# Initialize the list of prices
OutFun_prices = []

# Function to process a sale
def process_sale():
    
    global OutFun_total_price, OutFun_items, OutFun_quantities, OutFun_prices  # Declare as global variables

    # Clear the terminal
    clear_terminal()

    # Sets the total price to whatever OutFun_total_price is *Note OutFun_total_price is not in function
    total_price = OutFun_total_price
    items = OutFun_items
    quantities = OutFun_quantities
    prices = OutFun_prices


    
    # Ask the user for the name or code of the item
    while True:
        clear_terminal()
        # Print the current date and time
        print("Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("\n")

        # Print the sale process header
        print("New Sale")
        print("--------")

        # If n of items is >1 Print the items list header (Name, Quantity, Price, Total Price)
        if len(items) > 0:
            print("\nItems")
            print("-----")
            print("Name\t\tQuantity\tPrice\t\tTotal Price")
            # For every item in the list of items
            for i in range(len(items)):
                # Print the items name, quantity, price and total price
                print(f"{items[i][1]}\t\t{quantities[i]}\t\t{items[i][4]}\t\t{quantities[i] * float(items[i][4])}")
                # Add the total price of the item to the total price
                total_price += quantities[i] * float(items[i][4])
            # Print the total price in bold 
            print("\033[1m" + f"Total Price: {total_price}")
            print("\033[0m" + """""")


        item = input("Enter the name or code of the item or 'done' once finished, or type exit: ")
        # Searchs items.csv for the item by either its name or code. If input is letters search for name, if input is numbers search for code. Sets item to the item found in the csv file.
        # If input is a word
        if item == 'exit':
            import main_menu
            main_menu.main_menu()
        elif item == 'done':
            clear_terminal()

            # If no items have been added to the list warn the user if they wish to continue
            if len(items) == 0:
                input("No items have been added to the list.\n Click Enter to go back")
                process_sale()
            else:
                    # Print the order summary
                    print("Order Summary")
                    print("-------------")
                    print("\nItems")
                    print("-----")
                    print("Name\t\tQuantity\tPrice\t\tTotal Price")
                    # For every item in the list of items
                    for i in range(len(items)):
                        # Print the items name, quantity, price and total price
                        print(f"{items[i][1]}\t\t{quantities[i]}\t\t{items[i][4]}\t\t{quantities[i] * float(items[i][4])}")
                        # Add the total price of the item to the total price
                        total_price += quantities[i] * float(items[i][4])
                    # Print the total price in bold
                    print("\033[1m" + f"Total Price: {total_price}")
                    print("\033[0m" + """""")

                    # Ask if order went through
                    order = input("Did the order go through?\n1. Yes\n2. No\n")
                    # If the order didnt go through
                    if order == '2':
                        # Ask if the user wants to cancel the order or amend it
                        cancel = input("Do you want to cancel the order or amend it?\n1. Cancel\n2. Amend\nEnter your choice (1/2): ")
                        # If the user wants to cancel the order
                        if cancel == '1':
                            # Return to the main menu
                            import main_menu
                            main_menu.main_menu()
                        # If the user wants to amend the order
                        else:
                            # Return to the sale process
                            process_sale()
                    # Ask if it was cash or card
                    payment = input("Was the payment made by cash or card?\n1. Cash\n2. Card\nEnter your choice (1/2): ")
                    
                    # Create the 'Receipts' directory if it doesn't exist
                    if not os.path.exists('Receipts'):
                        os.makedirs('Receipts')

                    # Create a receipt file with the current date and time as the name
                    receipt_filename = f"Receipts/{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"
                    with open(receipt_filename, 'w', newline='') as file:
                        writer = csv.writer(file)
                        # Write the current date and time to the file
                        writer.writerow([f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
                        writer.writerow([])  # Empty row for spacing
                        # Write the items list header to the file
                        writer.writerow(["Items"])
                        writer.writerow(["Name", "Quantity", "Price", "Total Price"])
                        # For every item in the list of items
                        for i in range(len(items)):
                            # Write the items name, quantity, price and total price to the file
                            writer.writerow([items[i][1], quantities[i], items[i][4], quantities[i] * float(items[i][4])])
                        # Calculate and write GST (10% of the total price) to the file
                        gst = total_price * 0.1
                        writer.writerow([])  # Empty row for spacing
                        writer.writerow([f"GST: ${gst}"])
                        # Write the total price to the file
                        writer.writerow([f"Total Price: {total_price}"])
                        # Write the payment method to the file
                        if payment == '1':
                            writer.writerow(["Payment: Cash"])
                        else:
                            writer.writerow(["Payment: Card"])

                    # Print the receipt file name
                    print(f"Receipt saved as: {receipt_filename}")
                    # Wait for 5 seconds
                    time.sleep(5)
                    # Return to the main menu
                    import main_menu
                    main_menu.main_menu()
        # Else open items.csv THAT IS IN THE CSV_Files FOLDER and search for the item by its name if input is letters or by its code if input is numbers
        else:
            with open('CSV_Files/items.csv', 'r') as file:
                # If input is letters
                
                if item.isalpha():
                    #Search for the item by looking in the 2rd (1) coloum of the csv file (Named Item) and set item to the row
                    reader = csv.reader(file)
                    for row in reader:
                        if item in row[1]:
                            item = row
                            # Print the items name and price by looking at the 2nd (1) and 5th (4) coloum of the csv file
                            print(f"Item: {item[1]}")
                            print(f"Price: {item[4]}")
                            # Ask the user for the quantity of the item
                            quantity = int(input("Enter the quantity: "))
                            # Check if the item is already in the list of items
                            if item in items:
                                # If it is, add the quantity to the existing quantity
                                quantities[items.index(item)] += quantity
                            else:
                                # If it isn't, add the quantity to the list of quantities
                                quantities.append(quantity)
                                # Add the item to the list of items
                                items.append(item)
                            break
                    
                # If input is numbers find the item by looking in the 4th (3) coloum of the csv file (Named Code) and set item to the row
                else:
                    reader = csv.reader(file)
                    for row in reader:
                        if item in row[4]:
                            item = row
                            # Print the items name and price by looking at the 2nd (1) and 5th (4) coloum of the csv file
                            print(f"Item: {item[1]}")
                            print(f"Price: {item[4]}")
                            # Ask the user for the quantity of the item
                            quantity = int(input("Enter the quantity: "))
                            # Check if the item is already in the list of items
                            if item in items:
                                # If it is, add the quantity to the existing quantity
                                quantities[items.index(item)] += quantity
                            else:
                                # If it isn't, add the quantity to the list of quantities
                                quantities.append(quantity)
                                # Add the item to the list of items
                                items.append(item)
                            break
                


# Call the process_sale function
process_sale()

