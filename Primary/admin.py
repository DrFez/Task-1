
def edit_items_function():
    import Admin.edit_items_A as edit_items_A
    edit_items_A

def receipts_function():
    import Admin.receipt_A as receipt_A
    receipt_A

def stock_function():
    import Admin.stock_A as stock_A
    stock_A


def admin():
    if True:
        while True:
            print("\nAdmin:")
            print("1. Edit Items")
            print("2. Receipts")
            print("3. Stock")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

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
                import Primary.main_menu as main_menu
                main_menu.main_menu()
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
