import sqlite3

connection = sqlite3.connect('db.sqlite')


with open('dbconnection/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()



connection.commit()
connection.close()