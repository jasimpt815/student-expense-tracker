

# Expense Tracker

A simple menu driven Python application to track daily expenses
---

## Overview

Small daily expenses like snacks, bus fare, recharge, etc., can add up to a huge amount, but most people would not be able to remember where the money went exactly.

Expense Tracker is a lightweight console application built using Python. The user can enter their expenses with a name, amount, and category and the program will give insightful outputs such as total expense, highest expense, and expenses grouped by category.

It is implemented using only built-in Python libraries, and is organised as a collection of modules each implementing a specific feature.
---

## Features

| # | Feature | Description |
|---|---------|--------------|
| 1 | Add Expense | Adding an expense with name, amount, and category |
| 2 | View Expenses | Viewing all expenses in the session |

| 3 | Total Expenses | Calculating the total expense |
| 4 | Highest Expense | Finding the expense with the highest amount |
| 5 | Categorywise Expenses | Viewing the expenses grouped by their category |

| 6 | Exit | Exiting the program |
---
## Technologies / Tools Used
- Language: Python 3
- Concepts: functions, modules, lists, dictionaries, sets, loops, conditionals, taking input from the user
- Libraries: none (Python’s built-in libraries only)
- Version control: Git & GitHub
---
## Project Structure
```

expense-tracker/
├── main.py        # Menu loop
├── expense_add.py    # Add a new expense
├── expense_view.py    # View all expenses
├── expense_total.py   # Calculate total spending

├── expense_highest.py  # Find highest expense
├── expense_category.py  # Filter expenses by category
├── README.md       # Project documentation
└── statement.md     # Problem statement
```
---
## How to Install & Run
1. Install Python 3 (check version using `python --version` )
2. Clone the repository
```bash
git clone
cd expense-tracker
```
Or download the ZIP file from GitHub and extract the files. Keep all `.py` files in the same directory.

3. Run the program
```bash
python main.py
```
Problem Statement
Many people, especially students, spend money on little things every day and rarely keep track of it properly. After some time, they can't recall what they spent the most money on, how much was spent overall, or what percentage went into which category (eating out, traveling, etc). This makes it hard to control expenses and stay within the budget.

Spreadsheets and advanced financial programs can address these issues, but they are too bulky and time-consuming for simple day-to-day tracking.

Problem: Design and implement a simple, intuitive program, that would allow the user to log expenses with a short message/name, amount, and category, and calculate the total, find the largest expense, and display all expenses in a given category.

Scope of the Project:

In Scope
    
    Command-line (console) Python 3 application that:
    Records expenses with accompanying name/category
    Displays all expenses
    Calculates total spending amount
    Finds the largest/maximum expense
    Allows filtering of expenses by category (case-insensitive)
    Has a numbered menu with options that can handle incorrectly entered menu items
    Is modular, uses separate files for each module

Out of Scope (for this iteration)
    
    Permanent storage (files or DB) of the data; all data is held in memory during the session
    Graphical or web interface
    Updating, editing, or deleting expenses
    Working with dates, budgets, or visualizations
    Multi-user, authentication, server components

Target Users
    
    User Type Benefit
    Students Tracking of pocket money disbursements without the need for complex financial software
    Financial illiterate First steps in understanding their spending habits
    People who want to have a total sum of expenses at any given moment Quickly get an overview of their largest expenses and see how much they spent on     what
    Python learners Simple, clean, and well-structured program that uses modules and such core data structures as lists, dicts, and loops.
