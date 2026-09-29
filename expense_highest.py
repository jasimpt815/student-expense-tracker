def view_highest(expenses):
    costs=[]
    for i in expenses:
        costs.append(i["amount"])
    highest=max(costs)

    print("\nYour highest expense is", highest)

