import pandas as pd
import matplotlib.pyplot as plt

def add_expense(expenses, date, category, amount):
    expenses = expenses.append({
        'Date': date,
        'Category': category,
        'Amount': amount
    }, ignore_index=True)
    return expenses

def generate_report(expenses):
    # Group expenses by category and calculate the total amount for each category
    grouped_expenses = expenses.groupby('Category')['Amount'].sum().reset_index()

    # Plot a bar chart to visualize the expenses by category
    plt.bar(grouped_expenses['Category'], grouped_expenses['Amount'])
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Expense Report')
    plt.show()

# Create an empty DataFrame to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

while True:
    print("Expense Tracker Menu:")
    print("1. Add an expense")
    print("2. Generate expense report")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        date = input("Enter the date (MM/DD/YYYY): ")
        category = input("Enter the expense category: ")
        amount = float(input("Enter the expense amount: "))
        expenses = add_expense(expenses, date, category, amount)
        print("Expense added successfully.")
    elif choice == "2":
        generate_report(expenses)
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")