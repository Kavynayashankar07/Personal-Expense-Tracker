import csv
from datetime import datetime
import os

# Ensure CSV file exists
if not os.path.isfile("expenses.csv"):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Note"])  # header

# Function to add a new expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    note = input("Enter note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            print("\nDate\t\t\tAmount\tCategory\tNote")
            print("-"*60)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses found. Add some first!")

# Function to calculate total expenses
def total_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                total += float(row[1])
        print(f"\nTotal Expenses: {total}")
    except FileNotFoundError:
        print("No expenses found.")

# Menu for the user
def menu():
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    menu()
