from expense_tracker import ExpenseTracker
from datetime import datetime

def display_menu():
    print("\n--- Expense Tracker CLI ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Totals by Category")
    print("4. Plot Expenses (Pie Chart)")
    print("5. Plot Expenses (Bar Chart)")
    print("6. Exit")
    print("--------------------------")

def main_cli():
    tracker = ExpenseTracker() # Default to CSV, can be tracker = ExpenseTracker(file_format="json")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            date_str = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Transport): ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter description (optional): ")
            tracker.add_expense(date_str, category, amount, description)

        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            try:
                year = int(input("Enter year (e.g., 2023): "))
                month = int(input("Enter month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month. Please enter a number between 1 and 12.")
                    continue
                tracker.generate_report(report_type="monthly_category", year=year, month=month)
            except ValueError:
                print("Invalid input. Please enter valid numbers for year and month.")
        
        elif choice == '4':
            period_choice = input("Plot for (M)onthly or (A)ll time? (M/A): ").upper()
            if period_choice == 'M':
                try:
                    year = int(input("Enter year for plot (e.g., 2023): "))
                    month = int(input("Enter month for plot (1-12): "))
                    if not (1 <= month <= 12):
                        print("Invalid month. Please enter a number between 1 and 12.")
                        continue
                    tracker.plot_expenses(plot_type="pie", year=year, month=month)
                except ValueError:
                    print("Invalid input. Please enter valid numbers for year and month.")
            elif period_choice == 'A':
                tracker.plot_expenses(plot_type="pie")
            else:
                print("Invalid choice. Please enter 'M' or 'A'.")

        elif choice == '5':
            period_choice = input("Plot for (M)onthly or (A)ll time? (M/A): ").upper()
            if period_choice == 'M':
                try:
                    year = int(input("Enter year for plot (e.g., 2023): "))
                    month = int(input("Enter month for plot (1-12): "))
                    if not (1 <= month <= 12):
                        print("Invalid month. Please enter a number between 1 and 12.")
                        continue
                    tracker.plot_expenses(plot_type="bar", year=year, month=month)
                except ValueError:
                    print("Invalid input. Please enter valid numbers for year and month.")
            elif period_choice == 'A':
                tracker.plot_expenses(plot_type="bar")
            else:
                print("Invalid choice. Please enter 'M' or 'A'.")

        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_cli()