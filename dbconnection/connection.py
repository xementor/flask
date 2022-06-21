import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='md.zonaid',
    password='password',
    database='db'
)

cursor = db.cursor()
