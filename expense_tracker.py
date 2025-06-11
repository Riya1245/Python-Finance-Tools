import csv
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, filename="expenses.csv", file_format="csv"):
        self.filename = filename
        self.file_format = file_format.lower()
        self.expenses = self._load_expenses()

    def _load_expenses(self):
        """Loads expenses from the specified file."""
        expenses = []
        if self.file_format == "csv":
            try:
                with open(self.filename, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Ensure amount is float and date is datetime object
                        row['amount'] = float(row['amount'])
                        row['date'] = datetime.strptime(row['date'], '%Y-%m-%d').date()
                        expenses.append(row)
            except FileNotFoundError:
                print(f"No existing CSV file found: {self.filename}. A new one will be created.")
            except ValueError as e:
                print(f"Error reading CSV file (data format issue): {e}")
            except Exception as e:
                print(f"An unexpected error occurred while loading CSV: {e}")
        elif self.file_format == "json":
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for expense in data:
                        expense['amount'] = float(expense['amount'])
                        expense['date'] = datetime.strptime(expense['date'], '%Y-%m-%d').date()
                        expenses.append(expense)
            except FileNotFoundError:
                print(f"No existing JSON file found: {self.filename}. A new one will be created.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file: {e}. File might be corrupted or empty.")
            except ValueError as e:
                print(f"Error reading JSON file (data format issue): {e}")
            except Exception as e:
                print(f"An unexpected error occurred while loading JSON: {e}")
        else:
            print("Unsupported file format. Please use 'csv' or 'json'.")
        return expenses

    def _save_expenses(self):
        """Saves current expenses to the specified file."""
        if self.file_format == "csv":
            try:
                with open(self.filename, 'w', newline='') as f:
                    fieldnames = ['date', 'category', 'amount', 'description']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for expense in self.expenses:
                        # Convert date object back to string for saving
                        expense['date'] = expense['date'].strftime('%Y-%m-%d')
                        writer.writerow(expense)
            except IOError as e:
                print(f"Error writing to CSV file: {e}")
            except Exception as e:
                print(f"An unexpected error occurred while saving CSV: {e}")
        elif self.file_format == "json":
            try:
                # Convert date objects to strings before saving to JSON
                serializable_expenses = []
                for expense in self.expenses:
                    temp_expense = expense.copy()
                    temp_expense['date'] = temp_expense['date'].strftime('%Y-%m-%d')
                    serializable_expenses.append(temp_expense)

                with open(self.filename, 'w') as f:
                    json.dump(serializable_expenses, f, indent=4)
            except IOError as e:
                print(f"Error writing to JSON file: {e}")
            except Exception as e:
                print(f"An unexpected error occurred while saving JSON: {e}")

    def add_expense(self, date_str, category, amount, description=""):
        """Adds a new expense."""
        try:
            expense_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                return False

            new_expense = {
                'date': expense_date,
                'category': category.strip().lower(),
                'amount': amount,
                'description': description.strip()
            }
            self.expenses.append(new_expense)
            self._save_expenses()
            print(f"Expense added: {amount} in {category} on {date_str}")
            return True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
        except Exception as e:
            print(f"Error adding expense: {e}")
            return False

    def view_expenses(self, start_date=None, end_date=None):
        """Displays all recorded expenses or filters by date range."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        filtered_expenses = []
        for expense in self.expenses:
            if start_date and expense['date'] < start_date:
                continue
            if end_date and expense['date'] > end_date:
                continue
            filtered_expenses.append(expense)

        if not filtered_expenses:
            print("No expenses found for the specified date range.")
            return

        print("\n--- Your Expenses ---")
        for exp in filtered_expenses:
            print(f"Date: {exp['date'].strftime('%Y-%m-%d')}, Category: {exp['category'].capitalize()}, "
                  f"Amount: {exp['amount']:.2f}, Description: {exp['description']}")
        print("---------------------\n")

    def get_monthly_totals_by_category(self, year, month):
        """Calculates and returns monthly totals by category for a specific month."""
        monthly_totals = defaultdict(float)
        for expense in self.expenses:
            if expense['date'].year == year and expense['date'].month == month:
                monthly_totals[expense['category']] += expense['amount']
        return dict(monthly_totals) # Convert defaultdict to dict for cleaner output

    def generate_report(self, report_type="monthly_category", year=None, month=None):
        """Generates a summary report based on the type."""
        if report_type == "monthly_category":
            if year is None or month is None:
                print("Please provide year and month for monthly category report.")
                return

            totals = self.get_monthly_totals_by_category(year, month)
            if not totals:
                print(f"No expenses found for {month}/{year}.")
                return

            print(f"\n--- Monthly Report for {datetime(year, month, 1).strftime('%B %Y')} ---")
            for category, total in totals.items():
                print(f"{category.capitalize()}: {total:.2f}")
            print("-----------------------------------------\n")

    def plot_expenses(self, plot_type="pie", year=None, month=None):
        """Plots expenses using matplotlib."""
        if not self.expenses:
            print("No expenses to plot.")
            return

        data_for_plot = defaultdict(float)
        title = "All Time Expenses"

        if year and month:
            # Filter for a specific month
            for expense in self.expenses:
                if expense['date'].year == year and expense['date'].month == month:
                    data_for_plot[expense['category']] += expense['amount']
            title = f"Expenses for {datetime(year, month, 1).strftime('%B %Y')}"
        else:
            # All time expenses
            for expense in self.expenses:
                data_for_plot[expense['category']] += expense['amount']

        if not data_for_plot:
            print("No data to plot for the specified period.")
            return

        labels = list(data_for_plot.keys())
        sizes = list(data_for_plot.values())

        plt.figure(figsize=(8, 8)) # Optional: set figure size
        if plot_type == "pie":
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title(f"Expense Distribution ({title})")
        elif plot_type == "bar":
            plt.bar(labels, sizes)
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.title(f"Expenses by Category ({title})")
            plt.xticks(rotation=45, ha='right') # Rotate labels for readability
        else:
            print("Invalid plot type. Use 'pie' or 'bar'.")
            return

        plt.tight_layout() # Adjust layout to prevent labels from overlapping
        plt.show()