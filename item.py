from database import db, cursor

def add_item():
    name = input("Enter item name: ")
    rate = float(input("Enter rate: "))
    qty = int(input("Enter quantity: "))

    if rate <= 0 or qty <= 0:
        print("Invalid input!")
        return

    cursor.execute("INSERT INTO Item VALUES (NULL, %s, %s, %s)", (name, rate, qty))
    db.commit()

    print("Item added!")

def view_items():
    cursor.execute("SELECT * FROM Item")

    for row in cursor.fetchall():
        print(row)

def delete_item():
    code = int(input("Enter item code to delete: "))

    cursor.execute("SELECT * FROM Item WHERE item_code=%s", (code,))
    data = cursor.fetchone()

    if data is None:
        print("❌ Item not found!")
        return

    cursor.execute("DELETE FROM Item WHERE item_code=%s", (code,))
    db.commit()

    print("✅ Item deleted successfully!")