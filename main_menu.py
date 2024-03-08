
def sale_function():
    import sale
    sale

def admin_function():
    import admin
    admin

def main_menu():

    if True:
        while True:
            print("\nMain Menu:")
            print("1. Sale")
            print("2. Admin")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

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




