import mysql.connector

def connect_to_database():
    try:
        # Replace 'your_username', 'your_password', and 'your_host' with your actual MySQL credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password= '',
            database='contact_db'
        )

        if connection.is_connected():
            print(f"Connected to the 'contact_db' database")
            return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    # Call the function to connect to the database
    db_connection = connect_to_database()

    # Close the database connection when done
    if db_connection:
        db_connection.close()
        print("Connection closed")
