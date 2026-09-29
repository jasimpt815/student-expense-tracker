def add_expense(expenses):
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    expense_category = input("Enter expense category:")

    expense = {"name": expense_name, "amount": expense_amount,
               "category": expense_category}

    expenses.append(expense)
    print("Expense added successfully!")
