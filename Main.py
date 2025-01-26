import database
import ui
import analtyics

if __name__ == "__main__":
    connection = database.create_connection()
    if database.check_expense_exists(connection, expense_id=1):
        database.update_expense(connection, expense_id=1, new_category_id=1,
                                new_amount=180.00, new_description="Updated for groceries")
    else:
        print("Expense not found")
