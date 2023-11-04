import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  
            user='root',  
            password='', 
            database='ABHI'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None

def create_table(connection):
    create_table_query = """
    CREATE TABLE example_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_data(connection, name, age):
    insert_query = "INSERT INTO example_table (name, age) VALUES (%s, %s)"
    data = (name, age)
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def read_records(connection):
    select_query = "SELECT * FROM your_table"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

def update_record(connection, record_id, new_name, new_age):
    update_query = "UPDATE your_table SET name = %s, age = %s WHERE id = %s"
    data = (new_name, new_age, record_id)
    try:
        cursor = connection.cursor()
        cursor.execute(update_query, data)
        connection.commit()
        print("Record updated successfully")
    except Error as e:
        print(f"Error: {e}")

def delete_record(connection, record_id):
    delete_query = "DELETE FROM your_table WHERE id = %s"
    data = (record_id,)
    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, data)
        connection.commit()
        print("Record deleted successfully")
    except Error as e:
        print(f"Error: {e}")

def main():
    connection = create_connection()
    if connection is None:
        return

    create_table(connection)
    insert_data(connection, "John", 30)

    connection.close()
    print("Connection closed")

if __name__ == "__main__":
    main()