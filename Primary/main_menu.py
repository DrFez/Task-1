
def sale_function():
    import Primary.sale as sale
    sale

def admin_function():
    import Primary.admin as admin
    admin()

def main_menu():

    if True:
        while True:
            clear_terminal()
            print("\nMain Menu:")
            print("1. Sale")
            print("2. Admin")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")
            clear_terminal()
            if choice == '1':
                sale_function()
                break
            elif choice == '2':
                admin_function()
                break
            elif choice == '3':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


main_menu()



