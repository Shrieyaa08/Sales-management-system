from database import cursor

def show_sales():
    cursor.execute("SELECT * FROM Sales")
    data = cursor.fetchall()

    print("\nSales Report:")
    for row in data:
        print(row)