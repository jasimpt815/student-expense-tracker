# Project Statement: Expense Tracker

---

##  Problem Statement

Many people, especially students, spend money on small everyday items and rarely write these expenses down. Over time they lose track of how much they have spent, what their biggest purchase was, and which areas, such as food, travel or entertainment, take most of their money. Without this information it is hard to understand spending habits or stay within a budget.

Spreadsheets and full finance apps can solve this, but they often feel too heavy or time-consuming for quick daily use.

> **Problem:** Design and implement a simple, easy-to-use program that lets a user enter expenses with a name, amount and category, and then quickly find the total spent, the highest expense, and the expenses in any chosen category.

---

##  Scope of the Project

###  In Scope

- A command-line (console) application written in Python 3
- Recording expenses with a **name**, **amount** and **category**
- Viewing all recorded expenses
- Calculating the **total** spending
- Finding the **highest** expense
- **Filtering** expenses by category (case-insensitive)
- A repeating numbered menu with basic handling of invalid menu choices
- A modular code structure with one file per feature

###  Out of Scope (for this version)

- Saving data permanently (files or database). Data lives in memory for one session
- Graphical or web interface
- Editing or deleting expenses
- Dates, budgets, charts or reports
- Multiple users, login or cloud sync

---

##  Target Users

| User | How they benefit |
|------|------------------|
|  **Students** | Track pocket money and daily spending without complex tools |
|  **Beginners in personal finance** | Build the habit of recording expenses |
|  **Anyone wanting a quick tally** | Get totals and category summaries in seconds |
|  **Python learners** | A small, readable project showing modules, lists, dictionaries and loops |

---

##  High-Level Features

| # | Feature | Summary |
|---|---------|---------|
| 1 |  **Add Expense** | Enter name, amount and category to store an expense |
| 2 |  **View Expenses** | See a list of everything recorded |
| 3 |  **Total Expenses** | Get the sum of all expenses |
| 4 |  **Highest Expense** | Find the single most expensive item |
| 5 |  **Category-wise View** | Choose a category and see only its expenses |
| 6 |  **Exit** | Leave the program cleanly |

---

