import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="sales_db"
)

cursor = db.cursor()