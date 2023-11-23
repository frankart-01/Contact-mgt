import tkinter as tk
from tkinter import messagebox
import mysql.connector


def add_contact():
    # Get user input from the entry widgets
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()

    # Validate that all fields are filled
    if not all([first_name, last_name, email, phone_number]):
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='contact_db'
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # SQL query to insert a new contact into the 'contacts' table
        query = "INSERT INTO contacts (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email, phone_number)

        # Execute the query
        cursor.execute(query, values)

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Show a success message
        messagebox.showinfo("Success", "Contact added successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main application window
app = tk.Tk()
app.title("Add Contact")

# Create and configure GUI components
label_first_name = tk.Label(app, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_first_name = tk.Entry(app)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = tk.Label(app, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_last_name = tk.Entry(app)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(app, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(app)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_phone_number = tk.Label(app, text="Phone Number:")
label_phone_number.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_phone_number = tk.Entry(app)
entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI application
app.mainloop()
