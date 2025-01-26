import tkinter as tk
from tkinter import messagebox

class BudgetManager:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.balance = 0

    def set_income(self, income):
        self.income = income
        self.calculate_balance()

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.calculate_balance()

    def calculate_balance(self):
        total_expenses = sum(self.expenses.values())
        self.balance = self.income - total_expenses

    def get_summary(self):
        return {
            "Income": self.income,
            "Expenses": self.expenses,
            "Balance": self.balance
        }

def update_summary():
    summary = budget_manager.get_summary()
    income_label.config(text=f"Income: ₹{summary['Income']}")
    expenses_label.config(text=f"Expenses: ₹{sum(summary['Expenses'].values())}")
    balance_label.config(text=f"Balance: ₹{summary['Balance']}")

def set_income():
    try:
        income = float(income_entry.get())
        budget_manager.set_income(income)
        update_summary()
        income_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for income.")

def add_expense():
    try:
        category = expense_category_entry.get()
        amount = float(expense_amount_entry.get())
        if not category:
            messagebox.showerror("Invalid Input", "Please enter a category for the expense.")
            return
        budget_manager.add_expense(category, amount)
        update_summary()
        expense_category_entry.delete(0, tk.END)
        expense_amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for expense amount.")

# Initialize Budget Manager
budget_manager = BudgetManager()

# Create the GUI application window
app = tk.Tk()
app.title("Budget Management")
app.geometry("400x400")
app.resizable(False, False)

# Income Section
income_frame = tk.Frame(app)
income_frame.pack(pady=10)

income_label = tk.Label(income_frame, text="Income: ₹0", font=("Arial", 12))
income_label.pack()

income_entry = tk.Entry(income_frame, width=20)
income_entry.pack(pady=5)

set_income_button = tk.Button(income_frame, text="Set Income", command=set_income)
set_income_button.pack()

# Expense Section
expense_frame = tk.Frame(app)
expense_frame.pack(pady=10)

expenses_label = tk.Label(expense_frame, text="Expenses: ₹0", font=("Arial", 12))
expenses_label.pack()

expense_category_entry = tk.Entry(expense_frame, width=20)
expense_category_entry.insert(0, "Category")
expense_category_entry.pack(pady=5)

expense_amount_entry = tk.Entry(expense_frame, width=20)
expense_amount_entry.pack(pady=5)

add_expense_button = tk.Button(expense_frame, text="Add Expense", command=add_expense)
add_expense_button.pack()

# Balance Section
balance_frame = tk.Frame(app)
balance_frame.pack(pady=10)

balance_label = tk.Label(balance_frame, text="Balance: ₹0", font=("Arial", 12))
balance_label.pack()

# Run the application
app.mainloop()
