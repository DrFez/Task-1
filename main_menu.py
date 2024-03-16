
def sale_function():
    import sale
    sale

def admin_function():
    import admin
    admin.admin_menu()

def main_menu():

    if True:
        while True:
            #Prints Main Menu in BIG BOLD white
            print("\033[1m" + "Main Menu:")
            #Prints Sale in green
            print("\033[32m" + "1. Sale")
            #Prints Admin in purple
            print("\033[35m" + "2. Admin")
            #Prints Exit in red
            print("\033[31m" + "3. Exit")
            #Prints Enter your choice in white removing the bold
            choice = input("\033[0m" + "Enter your choice (1/2/3): ")

            clear_terminal()
            if choice == '1':
                sale_function()
                break
            elif choice == '2':
                admin_function()
                break
            elif choice == '3':
                print("Exiting program. Goodbye!")
                #Shut down Program compltelty 
                import sys
                sys.exit()
            else:
                #In Bold
                print("\033[1m" + "Invalid choice. Please enter 1, 2, or 3.\n")
                print("\033[0m" + """\n""")

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
main_menu()



