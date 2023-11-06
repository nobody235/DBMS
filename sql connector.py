import mysql.connector

connection = mysql.connector.connect( host='127.0.0.1', user='root', password='', database='ABHI')
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Couldn't connect to the database")

cursor = connection.cursor()
cursor.execute("CREATE TABLE example_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, age INT)")
print("Table created successfully")

cursor.execute("INSERT INTO example_table VALUES (1, 'Abhi', 21)")
connection.commit()
print("Data inserted successfully")

cursor.execute("INSERT INTO example_table VALUES (2, 'ABC', 30)")
connection.commit()
print("Data inserted successfully")


cursor.execute("SELECT * FROM example_table")
records = cursor.fetchall()
for record in records:
    print(record)

cursor.execute("UPDATE example_table SET name = 'Aryan', age = 13 WHERE id = 1")
connection.commit()
print("Record updated successfully")

cursor.execute("DELETE FROM example_table WHERE id = 2")
connection.commit()
print("Record deleted successfully")

connection.close()
print("Connection closed")