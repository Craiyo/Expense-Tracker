import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",         # Replace with your MySQL host
            user="root",     # Replace with your MySQL username
            password="2003", # Replace with your MySQL password
            database="budget" # Replace with your database name
        )
        if connection.is_connected():
            print("Connected to MySQL Database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_category(connection, name):
    cursor = connection.cursor()
    query = "INSERT INTO categories (name) VALUES (%s)"
    try:
        cursor.execute(query, (name,))
        connection.commit()
        print(f"Category '{name}' added successfully")
    except Error as e:
        print(f"Error: {e}")

def add_expense(connection, date, category_id, amount, description):
    cursor = connection.cursor()
    query = """
    INSERT INTO expenses (date, category_id, amount, description)
    VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (date, category_id, amount, description))
        connection.commit()
        print("Expense added successfully")
    except Error as e:
        print(f"Error: {e}")

def fetch_expenses(connection):
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT e.id, e.date, c.name AS category, e.amount, e.description
    FROM expenses e
    JOIN categories c ON e.category_id = c.id
    ORDER BY e.date DESC
    """
    cursor.execute(query)
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

def update_category(connection, category_id, new_name):
    cursor = connection.cursor()
    query = "UPDATE categories SET name = %s WHERE id = %s"
    try:
        cursor.execute(query, (new_name, category_id))
        connection.commit()
        print(f"Category ID {category_id} updated to '{new_name}'")
    except Error as e:
        print(f"Error: {e}")

def delete_expense(connection, expense_id):
    cursor = connection.cursor()
    query = "DELETE FROM expenses WHERE id = %s"
    try:
        cursor.execute(query, (expense_id,))
        connection.commit()
        print(f"Expense ID {expense_id} deleted successfully")
    except Error as e:
        print(f"Error: {e}")

def update_expense(connection, expense_id, new_category_id=None, new_amount=None, new_description=None):
    cursor = connection.cursor()

    # Construct the SQL query dynamically based on provided fields
    query = "UPDATE expenses SET "
    update_fields = []
    update_values = []

    if new_category_id:
        update_fields.append("category_id = %s")
        update_values.append(new_category_id)
    
    if new_amount:
        update_fields.append("amount = %s")
        update_values.append(new_amount)
    
    if new_description:
        update_fields.append("description = %s")
        update_values.append(new_description)
    
    # Combine the SET parts and prepare the full query
    query += ", ".join(update_fields) + " WHERE id = %s"
    update_values.append(expense_id)

    try:
        cursor.execute(query, tuple(update_values))
        connection.commit()
        print(f"Expense ID {expense_id} updated successfully")
    except Error as e:
        print(f"Error updating expense: {e}")

def delete_category_set_default(connection, category_id):
    cursor = connection.cursor()
    
    # Step 1: Check if default category exists, if not, create it
    default_category_name = "Uncategorized"
    check_default_query = "SELECT id FROM categories WHERE name = %s"
    cursor.execute(check_default_query, (default_category_name,))
    default_category = cursor.fetchone()
    
    if not default_category:
        # Create the default category
        insert_default_query = "INSERT INTO categories (name) VALUES (%s)"
        cursor.execute(insert_default_query, (default_category_name,))
        connection.commit()
        default_category_id = cursor.lastrowid
        print(f"Default category '{default_category_name}' created with ID {default_category_id}")
    else:
        default_category_id = default_category[0]

    # Step 2: Reassign all expenses to the default category
    update_query = """
    UPDATE expenses
    SET category_id = %s
    WHERE category_id = %s
    """
    try:
        cursor.execute(update_query, (default_category_id, category_id))
        connection.commit()
        print(f"All expenses reassigned to default category ID {default_category_id}")
    except Error as e:
        print(f"Error updating expenses: {e}")
        return

    # Step 3: Delete the category
    delete_query = "DELETE FROM categories WHERE id = %s"
    try:
        cursor.execute(delete_query, (category_id,))
        connection.commit()
        print(f"Category ID {category_id} deleted successfully")
    except Error as e:
        print(f"Error deleting category: {e}")

def check_expense_exists(connection, expense_id):
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM expenses WHERE id = %s"
    cursor.execute(query, (expense_id,))
    return cursor.fetchone()[0] > 0

