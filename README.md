

#  Expense Tracker

**A simple, menu-driven Python app to record and analyse your everyday spending**


---

##  Overview

Small daily purchases like snacks, bus fares and recharges add up quickly, and most people can't say where their money went at the end of the month.

**Expense Tracker** is a lightweight console application written in Python. You enter each expense with a **name**, an **amount** and a **category**, and the program instantly gives you useful answers: your total spending, your biggest expense, and everything you spent in a chosen category.

It uses only built-in Python, so there is nothing to install. The code is split into small modules, one per feature, which keeps it clean and easy to extend.

---

##  Features

| # | Feature | What it does |
|---|---------|--------------|
| 1 | **Add Expense** | Record an expense with name, amount and category |
| 2 | **View Expenses** | List every expense recorded in the session |
| 3 | **Total Expenses** | Show the sum of all expenses |
| 4 | **Highest Expense** | Find the single largest expense |
| 5 | **Category-wise Expenses** | List available categories and filter expenses by one (case-insensitive) |
| 6 | **Exit** | Close the program cleanly |

---

##  Technologies / Tools Used

- **Language:** Python 3
- **Concepts:** functions, modules, lists, dictionaries, sets, loops, conditionals, user input
- **Libraries:** none (Python standard library only)
- **Version control:** Git & GitHub

---

## Project Structure

```
expense-tracker/
├── main.py               # Menu loop, controller
├── expense_add.py        # Add a new expense
├── expense_view.py       # View all expenses
├── expense_total.py      # Calculate total spending
├── expense_highest.py    # Find highest expense
├── expense_category.py   # Filter expenses by category
├── README.md             # Project documentation
└── statement.md          # Problem statement
```

---

##  How to Install & Run

**1. Make sure Python 3 is installed**

```bash
python --version
```

**2. Get the project**

```bash
git clone <your-repository-link>
cd expense-tracker
```

Or download the ZIP from GitHub and extract it. Keep all `.py` files in the same folder.

**3. Run the program**

```bash
python main.py
```

*(On some systems use `python3 main.py`.)*

---

##  How to Use

When the program starts you will see this menu:

```
Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Highest Expense
5. Categorywise Expenses
6. Exit

Enter your choice (1-6):
```

Type a number and press **Enter**. The menu returns after each action until you choose **6**.

>  Data is stored in memory only, so expenses are cleared when you exit the program.

---

## Instructions for Testing

Testing is manual. Run `python main.py` and try the cases below.

| # | Test | Steps | Expected result |
|---|------|-------|-----------------|
| 1 | Add expense | Option `1` → `Lunch`, `150`, `Food` | `Expense added successfully!` |
| 2 | View expenses | Option `2` | All added expenses are printed |
| 3 | View when empty | Option `2` on a fresh run | `No expenses recorded.` |
| 4 | Total | Add `150`, `40.5`, `300`, then option `3` | `Total Expenses: 490.5` |
| 5 | Highest | Same data, option `4` | `Your highest expense is 300.0` |
| 6 | Category filter | Option `5` → `Food` | Only the Food expenses are shown |
| 7 | Unknown category | Option `5` → `Health` | `No expenses of this category` |
| 8 | Invalid choice | Enter `9` or `abc` at the menu | `Invalid choice. Please try again.` |
| 9 | Exit | Option `6` | `Exiting the program.` |

---

## Screenshots

> Replace the blocks below with real screenshots of your terminal, for example `![Menu](screenshots/menu.png)`.

**Main menu and adding an expense**

```
Enter your choice (1-6): 1
Enter the name of the expense: Lunch
Enter the amount of the expense: 150
Enter expense category: Food
Expense added successfully!
```

**Viewing expenses, total and highest**

```
YOUR EXPENSES
{'name': 'Lunch', 'amount': 150.0, 'category': 'Food'}
{'name': 'Bus Ticket', 'amount': 40.5, 'category': 'Travel'}
{'name': 'Movie', 'amount': 300.0, 'category': 'Entertainment'}

Total Expenses: 490.5
Your highest expense is 300.0
```

---

## Known Limitations

- Data is not saved between sessions.
- Entering a non-numeric amount stops the program.
- Choosing *Highest Expense* before adding any expense stops the program.

---

## Future Enhancements

- Input validation and friendlier error messages
- Save and load data with a CSV/JSON file or SQLite database
- Add dates, plus monthly and weekly summaries
- Edit and delete expenses
- Category-wise totals and budget alerts
- Charts, or a graphical / web interface

---

