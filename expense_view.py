def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\nYOUR EXPENSES")

    for expense in expenses:
        print(expense)
