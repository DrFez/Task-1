
def edit_items_function():
    import edit_items_A
    edit_items_A.items_menu()

def receipts_function():
    import receipt_A
    receipt_A

def stock_function():
    import stock_A
    stock_A.stock_menu()

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_menu():
    if True:
        clear_terminal()
        while True:
            #Prints Admin in purple
            print("\033[35m" + "Admin Menu:")
            #Prints Edit Items in white
            print("\033[37m" + "1. Edit Items")
            print("2. Receipts")
            print("3. Stock")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")
            clear_terminal()

            if choice == '1':
                edit_items_function()
                break
            elif choice == '2':
                receipts_function()
                break
            elif choice == '3':
                stock_function()
                break
            elif choice == '4':
                import main_menu
                main_menu.main_menu()
                break
            else:
                print("\033[1m" + "Invalid choice. Please enter 1, 2, or 3.")
                print("\033[0m" + """""")

admin_menu()
