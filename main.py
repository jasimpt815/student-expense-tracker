import expense_total
import expense_view
import expense_add
import expense_highest
import expense_category
expenses = []


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Highest Expense")
        print("5. Categorywise Expenses")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            expense_add.add_expense(expenses)
        elif choice == "2":
            expense_view.view_expenses(expenses)
        elif choice == "3":
            expense_total.calculate_total(expenses)
        elif choice == "4":
            expense_highest.view_highest(expenses)
        elif choice == "5":
            expense_category.category_filter(expenses)

        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
