from item import add_item, view_items,delete_item
from sales import create_bill
from report import show_sales

while True:
    print("\n====== SALES MANAGEMENT SYSTEM ======")
    print("1. Add Item")
    print("2. View Items")
    print("3. Delete Item")
    print("4. Create Bill")
    print("5. Sales Report")
    print("6. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_item()

    elif choice == 2:
        view_items()

    elif choice == 3:
       delete_item()

    elif choice == 4:
       create_bill()

    elif choice == 5:
       show_sales()

    elif choice == 6:
       break