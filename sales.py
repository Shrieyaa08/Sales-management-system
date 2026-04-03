from database import db, cursor

def create_bill():
    total = 0

    n = int(input("Enter number of items: "))

    for i in range(n):
        code = int(input("Enter item code: "))
        qty = int(input("Enter quantity: "))

        cursor.execute("SELECT rate, quantity FROM Item WHERE item_code=%s", (code,))
        data = cursor.fetchone()

        if data is None:
            print("Item not found!")
            continue

        rate, stock = data

        if qty > stock:
            print("Not enough stock!")
            continue

        amount = rate * qty
        total = total + amount

        cursor.execute("UPDATE Item SET quantity = quantity - %s WHERE item_code=%s", (qty, code))

    cursor.execute("INSERT INTO Sales VALUES (NULL, CURDATE(), %s)", (total,))
    db.commit()

    print("Bill created!")
    print("Total amount =", total)