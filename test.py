import sqlite3

#database
conn = sqlite3.connect("Contacts.db")

my_cursor = conn.cursor()

#sql
my_cursor.execute("SELECT * FROM Persons")

show = my_cursor.fetchall()

print(show)