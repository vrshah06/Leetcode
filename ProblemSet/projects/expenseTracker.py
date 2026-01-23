import csv
from datetime import datetime
file_name="expenses.csv"
def show_menu():
    print("Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total spent")
    print("4. Filter by Category")
    print("5. Exit")
def add_expense():
    Category = input("Enter category (e.g., Food, Transport): ")
    Amount = float(input("Enter amount: "))
    note= input("Enter note/description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name,'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, Category, Amount, note])
    print("✅ Expense added successfully.")
def view_expenses():
    try:
        with open(file_name,'r') as file:
            reader = csv.reader(file)
            print("Date\t\t\tCategory\tAmount\tNote")
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
def total_spent():
    total=0
    try:
        with open(file_name,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"Total spent: Rs {total:.2f}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")
def filter_by_category():
    category = input("Enter category to filter by: ")
    found = False
    total_spent_category = 0
    try:
        with open(file_name,'r') as file:
            reader = csv.reader(file)
            print("Date\t\t\tCategory\tAmount\tNote")
            for row in reader:
                if row[1].lower() == category.lower():
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
                    total_spent_category += float(row[2])

                    found = True
        if not found:
            print(f"No expenses found for category: {category}")
        else:
            print(f"Total spent in category {category}: Rs {total_spent_category:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_spent()
    elif choice == '4':
        filter_by_category()
    elif choice == '5':
        print("👋👋 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
