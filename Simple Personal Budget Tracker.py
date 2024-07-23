class BudgetTracker:
    def _init_(self):
        self.income = 0
        self.expenses = []
        self.total_expenses = 0

    def add_income(self):
        try:
            amount = float(input("Enter income amount: "))
            self.income += amount
            print(f"Income added. Total income: ${self.income:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def add_expense(self):
        try:
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            self.expenses.append({"description": description, "amount": amount})
            self.total_expenses += amount
            print(f"Expense added. Total expenses: ${self.total_expenses:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def view_summary(self):
        print("\nFinancial Summary")
        print("=================")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.total_expenses:.2f}")
        print(f"Net Savings: ${self.income - self.total_expenses:.2f}")
        print("\nDetailed Expenses:")
        for expense in self.expenses:
            print(f"  {expense['description']}: ${expense['amount']:.2f}")
        print("=================\n")

def main():
    tracker = BudgetTracker()
    while True:
        print("Personal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            tracker.add_income()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if _name_ == "_main_":
    main()
